FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
COPY . /home
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6
WORKDIR /home
RUN pip install -r requirements.txt
RUN pip install --upgrade --no-cache-dir gdown
RUN python3 setup.py develop --no_cuda_ext
RUN pip install streamlit
RUN python3 -c "import gdown;gdown.download('https://drive.google.com/uc?id=14D4V4raNYIOhETfcuuLI3bGLB-OYIv6X', './experiments/pretrained_models/', quiet=False)"
CMD [ "streamlit", "run", "app.py" ]