# 2019.1-Lino [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
O projeto Lino é um bot que visa orientar, alertar e tirar dúvidas a respeito dos assuntos mais procurados na Universidade de Brasília - Campus FGA

## Instalação

### 1 - build imagem server actions: `sudo docker build -t jp:latest .`

### 2 - build imagem telegram server: `sudo docker build -t telegram-jp:latest -f Telegram.Dockerfile .`

### 3 - build imagem intercampi server: `sudo docker build -t jp-intercampi:latest -f Telegram.Dockerfile .`

### 4 - Run ngrok with `./ngrok http 5000`

### 5 - Run ngrok with `./ngrok http 5055`

### 6 - Run ngrok with `./ngrok http 5002`

### 7 - Substituir as urls com HTTPS no .env juntamente com o token do seu bot

### 8 -Pegar a url HTTPS no ngrok na porta 5000 e o token do bot e substituir na url: `https://api.telegram.org/bot{token}/setWebhook?url={}`

#### Obs: substituir e retirar as chaves {}

### 9 - rodar compose: `sudo docker-compose up`
