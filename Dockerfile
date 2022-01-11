FROM python:latest

SHELL ["/bin/bash", "-c"]

RUN apt update && apt install -y \
    python3-opencv \
    libgl1-mesa-glx

COPY ./resource/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./resource/start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]

WORKDIR /workspace
