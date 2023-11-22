FROM python:3.11.6

# build-essential
RUN apt-get update \
    && apt-get install -y build-essential wget

# install cmake
# Install cmake
RUN wget https://cmake.org/files/v3.23/cmake-3.23.0-linux-x86_64.sh \
    && chmod +x cmake-3.23.0-linux-x86_64.sh \
    && ./cmake-3.23.0-linux-x86_64.sh --skip-license --prefix=/usr/local \
    # Uncomment the line below for debugging
    # && ls -l cmake-3.23.0-linux-x86_64.sh \
    && rm cmake-3.23.0-linux-x86_64.sh \
    # Uncomment the line below for debugging
    # && cmake --version

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
