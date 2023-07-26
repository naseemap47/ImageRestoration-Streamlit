import streamlit as st
from basicsr.models import create_model
from basicsr.utils import img2tensor as _img2tensor, tensor2img
from basicsr.utils.options import parse
import numpy as np
import cv2


def img2tensor(img, bgr2rgb=False, float32=True):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.
    return _img2tensor(img, bgr2rgb=bgr2rgb, float32=float32)

def single_image_inference(model, img):
	model.feed_data(data={'lq': img.unsqueeze(dim=0)})

	if model.opt['val'].get('grids', False):
		model.grids()

	model.test()

	if model.opt['val'].get('grids', False):
		model.grids_inverse()

	visuals = model.get_current_visuals()
	sr_img = tensor2img([visuals['result']])
	return sr_img


opt_path = 'options/test/REDS/NAFNet-width64.yml'
opt = parse(opt_path, is_train=False)
opt['dist'] = False
NAFNet = create_model(opt)

################## APP ##################
st.title('Unblur Image - NAFNet')

# Upload image
upload_img_file = st.file_uploader(
    'Upload Image', type=['jpg', 'jpeg', 'png'])
FRAME_WINDOW = st.image([], channels='BGR')

if upload_img_file is not None:
    file_bytes = np.asarray(
        bytearray(upload_img_file.read()), dtype=np.uint8)
    img_input = cv2.imdecode(file_bytes, 1)
    FRAME_WINDOW.image(img_input, channels='BGR')

    if st.button('Submit', use_container_width=True):
        st.subheader('Result')
        inp = img2tensor(img_input)
        out_img = single_image_inference(NAFNet, inp)
        st.image(out_img, channels='BGR')
