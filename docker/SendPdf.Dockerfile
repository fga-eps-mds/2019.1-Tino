FROM python:3.6

LABEL AUTHOR="jp-gomes" 


#Instalando pacotes necessários
RUN pip install --upgrade pip && \
    pip install flask && \ 
    pip install request

RUN mkdir /2019.1-Tino

ADD . /2019.1-Tino

WORKDIR /2019.1-Tino


