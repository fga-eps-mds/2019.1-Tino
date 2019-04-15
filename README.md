# 2019.1-Lino [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
O projeto Lino é um bot que visa orientar, alertar e tirar dúvidas a respeito dos assuntos mais procurados na Universidade de Brasília - Campus FGA

## Instalação

### 1 - build imagem server actions: `sudo docker build -t jp:latest .`

### 2 - build imagem telegram server: `sudo docker build -t telegram-jp:latest -f Telegram.Dockerfile .`

### 3 - Run ngrok with `./ngrok http 5000`

### 4 - Get https url and set webhook with following url: `https://api.telegram.org/bot{token}/setWebhook?url=https://77dc50cf.ngrok.io`

### 5 - rodar compose: `sudo docker-compose up`
