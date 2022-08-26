FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt update && apt install tmux -y

RUN echo "set -g mouse on" >> /root/.tmux.conf

WORKDIR /root