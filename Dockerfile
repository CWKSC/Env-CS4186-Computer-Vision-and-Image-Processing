FROM python:latest

# https://gradle.org/install/

ENV GRADLE_VERSION=7.3.3

SHELL ["/bin/bash", "-c"]

COPY ./resource/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./resource/start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]

WORKDIR /workspace
