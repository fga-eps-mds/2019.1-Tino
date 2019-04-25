FROM python:3.6

LABEL AUTHOR="jp-gomes" 

# Adicionando requirements txt ao projeto
ADD ./requirements.txt /tmp

#Instalando pacotes necessários
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    pip install rasa_core_sdk && \
    pip install flask && \
    pip install pandas && \
    pip install python-dotenv && \
    pip install pandas && \
    python -m spacy download pt

RUN mkdir /2019.1-Tino

ADD . /2019.1-Tino

WORKDIR /2019.1-Tino

#python -m rasa_nlu.train -c nlu/nlu_config.yml --data nlu/nlu_data.md -o models --fixed_model_name nlu --project current --verbose
#python -m rasa_core.train -d core/domain.yml -s core/stories.md -o models/current/dialogue
#python -m rasa_core_sdk.endpoint --actions actions
#python main.py

