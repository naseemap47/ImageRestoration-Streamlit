# ImageRestoration-Streamlit
[<img src="https://img.shields.io/badge/Docker-Image-blue.svg?logo=docker">](<https://hub.docker.com/repository/docker/naseemap47/streamlit-nafnet>) <br>
Restore image using NAFNet model with streamlit dashboard

## Installtion
1. **Clone this Repo**
```
git clone https://github.com/naseemap47/ImageRestoration-Streamlit.git
cd ImageRestoration-Streamlit
```
2. **Install Libraries**
```
pip install -r requirements.txt
pip install --upgrade --no-cache-dir gdown
python3 setup.py develop --no_cuda_ext
```
## Download pretrained models
```
import gdown
gdown.download('https://drive.google.com/uc?id=14D4V4raNYIOhETfcuuLI3bGLB-OYIv6X', "./experiments/pretrained_models/", quiet=False)
```
## Run Dashboard
```
streamlit run app.py
```