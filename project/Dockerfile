FROM python:3.6

RUN pip install rasa_core

RUN pip install rasa_nlu[spacy] && \
    python -m spacy download pt

RUN pip install rasa_nlu[tensorflow]

RUN pip install pymongo
RUN pip install requests

RUN mkdir /2019.1-Tino

ADD . /2019.1-Tino

WORKDIR /2019.1-Tino

ENV TRAINING_EPOCHS=100 \
    CREDENTIALS="./project/config/credentials.yml"

CMD python train.py all && python train-telegram.py
