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
2. **Install Libraries**<br>

**With pip**
```
pip install torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117
pip install -r requirements.txt
pip install --upgrade --no-cache-dir gdown
python3 setup.py develop --no_cuda_ext
pip install streamlit
```
**With conda (Recommended)**
```
conda create -n app python=3.9 -y
conda activate app

# Linux and Windows
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia
# OSX
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 -c pytorch

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
