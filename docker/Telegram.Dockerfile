FROM python:3.6

LABEL AUTHOR="jp-gomes" 

# Adicionando requirements txt ao projeto
ADD ./requirements.txt /tmp

#Instalando pacotes necessários
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    pip install pandas && \
    pip install python-dotenv && \
    python -m spacy download pt

RUN mkdir /2019.1-Tino

ADD . /2019.1-Tino

WORKDIR /2019.1-Tino



