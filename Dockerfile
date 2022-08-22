FROM dorowu/ubuntu-desktop-lxde-vnc:latest

USER root

RUN apt-key adv --fetch-keys https://dl.google.com/linux/linux_signing_key.pub

RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    fonts-noto-cjk fonts-noto-cjk-extra language-selector-common language-pack-ja wget \
 && update-locale LANG=ja_JP.UTF-8 \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*


ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo
