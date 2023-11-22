FROM ubuntu:latest

# set environment variables
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y python3-dev \
    && apt-get install -y python3-pip \
    && apt-get install -y python3-setuptools \
    && apt-get install -y python3-wheel

# install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg

COPY . /app/
WORKDIR /app/

# install requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# run
CMD python3 -m WinxMusic
