FROM lixiepeng/lxp:rasa-zh-base

ADD . /work

WORKDIR /work

EXPOSE 5000
EXPOSE 5005
EXPOSE 5500

# CMD [ "python", "./webchat.py" ]


RUN apt-get update && apt-get install -y -f --no-install-recommends --fix-missing \
    graphviz \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*


RUN pip install -r requirements.txt