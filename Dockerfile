FROM python:3.11.6

# install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg

COPY . /app/
WORKDIR /app/

# upgrade pip
RUN pip3 install --no-cache-dir -U pip

# install requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# run
CMD python3 -m WinxMusic
