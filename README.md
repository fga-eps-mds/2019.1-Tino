# 2019.1-Tino [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Tino é um bot desenvolvido por alunos da FGA-Gama que consegue orientar sobre os horários e destinos do intercampi dos diversos campus da Universidade de Brasília, além de conseguir informar horário de atendimento, sala e contato dos professores que forem cadastrados no bot.

Esse repositório contém o código do framework do chatbot Tino, e todos os seus microserviços utilizados.

### Tecnologias utilizadas
<ul>
  <li> Rasa Core (Fluxo de conversa) </li>
  <li> Rasa NLU ( Processamento e extração de informações) </li>
  <li> Flask (microframework utilizado para os microserviços) </li>
  <li> MongoDB (NoSQL database) </li>
</ul>
    
    
### Entenda um pouco da arquitetura:
<a href="https://ibb.co/WyTpYBM"><img src="https://i.ibb.co/yy3BbgZ/architecture-3.png" alt="architecture-3" border="0"></a>
    
### Para testar a Tino utiizando o telegram, siga os seguintes comandos para subir os containers em seu computador:

#### 1 - Construir imagem do telegram: `sudo docker build -t telegram-jp:latest -f Telegram.Dockerfile .`

#### 2 - Construir a imagem das ações personalizadas do RASA: `sudo docker build -t jp:latest .`

#### 3 - Construir a imagem do microserviço que informa o intercampi: `sudo docker build -t jp-intercampi:latest -f Intercampi.Dockerfile .`

#### 4 - Construir a imagem do microserviço que envia uma imagem com o horário de todos os intercampis: `sudo docker build -t jp-send-pdf:latest -f SendPdf.Dockerfile .`

#### 5 - Com todas as imagens prontas para serem utilizadas, precisamos utilizar uma conexão segura para utilizar como webhook para o telegram, iremos utilizar um pequeno programinha de linha de comando que permite criar um túnel de conexão segura a partir do seu localhost chamado NGROK. (Você encontra a instalação neste link <a href="https://ngrok.com/download" target="_blank">Install ngrok</a>

#### 6 - Com o ngrok instalado, vamos rodar utilizando o seguinte comando: `./ngrok http 5000` (5000 é a porta padrão, caso você tenha alterado o docker-compose.yml, o telegram irá escutar o webhook em outra porta)

#### 7 - Ufa, agora sim podemos subir nossos containers e ser feliz `sudo docker-compose up` para subir todos os containers (incluindo o banco de dados mongo e o redis)


