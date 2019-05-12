FROM python:3.6

LABEL AUTHOR="jp-gomes" 

# Adicionando requirements txt ao projeto
ADD ./requirements.txt /tmp

#Instalando pacotes necessários
RUN pip install --upgrade pip && \ 
	pip install pandas && \   
    pip install flask && \
    pip3 install pymongo && \
    pip install python-dotenv && \
    pip install lxml && \
    pip install html5lib && \
    pip install BeautifulSoup4

RUN mkdir /2019.1-Tino

ADD . /2019.1-Tino

WORKDIR /2019.1-Tino


