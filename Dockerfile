FROM ubuntu:18.04

LABEL maintainer="Showyou <showyou41@gmail.com>"

ENV LANG=C.UTF-8

RUN apt update && apt install -y tzdata
ENV TZ=Asia/Tokyo

RUN apt update && apt install -y jupyter-notebook && \
    groupadd -r jupyter && useradd --no-log-init -r -m -g jupyter jupyter
USER jupyter
WORKDIR /home/jupyter
#RUN ls -al
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0"]
