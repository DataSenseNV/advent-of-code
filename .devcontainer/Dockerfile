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

RUN useradd -m -d /home/jim -p jim -s /bin/bash jim
RUN usermod -aG sudo jim

USER jim

RUN echo "export PATH=/home/jim/.local/bin:$PATH" >> /home/jim/.bashrc

WORKDIR /workspace

EXPOSE 8080

CMD ["/bin/bash"]