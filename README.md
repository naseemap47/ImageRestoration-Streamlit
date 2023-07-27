# ImageRestoration-Streamlit
[<img src="https://img.shields.io/badge/Docker-Image-blue.svg?logo=docker">](<https://hub.docker.com/repository/docker/naseemap47/streamlit-nafnet>) <br>
Restore image using NAFNet model with streamlit dashboard

## Dashboard
![demo](https://github.com/naseemap47/ImageRestoration-Streamlit/assets/88816150/6081cfa5-96f8-4ff0-ba5c-d85723e025aa)

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
pip install streamlit
```
## Download pretrained models
```
python3 -c "import gdown;gdown.download('https://drive.google.com/uc?id=14D4V4raNYIOhETfcuuLI3bGLB-OYIv6X', './experiments/pretrained_models/', quiet=False)"
```
## Run Dashboard
```
streamlit run app.py
```
## User Guide
1. Upload image - (Click -> **Browse files**)
2. To restore image (Click -> **Submit**)
3. Download restored image - (Click -> **Download Image**)
