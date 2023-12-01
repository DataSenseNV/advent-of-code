FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -y install --no-install-recommends \
    build-essential \
    sudo \
    curl \
    apt-utils \
    git \
    procps \
    gcc \
    python3.11 \
    python3-pip \
    python3.11-dev \
    openjdk-17-jdk \
    unixodbc-dev
RUN apt autoremove -y 
RUN apt clean
RUN rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

RUN useradd -m -d /home/coder -p coder -s /bin/bash coder
RUN usermod -aG sudo coder

USER coder

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN echo "export PATH=/home/coder/.local/bin:$PATH" >> /home/coder/.bashrc

COPY python/requirements.txt /home/coder/requirements.txt

RUN python3.11 -m pip install -r /home/coder/

COPY jupyter_notebook_config.py /home/coder/.local/lib/python3.11/site-packages/

WORKDIR /workspace

EXPOSE 8888

CMD ["/bin/bash"]