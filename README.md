# 2019.1-Tino [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<p align="center">
  <img src="http://tino-1-2019.com.br/wp-content/uploads/2019/04/logowolf-uai-258x254.png">
</p>
<h1 align="center"> Tino - O Bot </h1>
<p align="center">
  <img width="35" src="https://user-images.githubusercontent.com/18364727/46376121-9a759e80-c66b-11e8-8aa0-6c4cf887089e.png">
</p>

### Sobre o projeto

<p align="justify"> &emsp;&emsp;
   Tino é um bot desenvolvido por alunos da FGA-Gama que consegue orientar sobre os horários e destinos do intercampi dos diversos campus da Universidade de Brasília, além de conseguir informar horário de atendimento, sala e contato dos professores que forem cadastrados no bot. Este repositório contém o código do framework do chatbot Tino, e todos os seus microserviços utilizados.</p>


### Utilização

&emsp;&emsp; O Tino se encontra na plataforma <a href="https://web.telegram.org/#/im?p=@tino_bot">Telegram</a>

### Principais funcionalidades
<html>
 <ul>
  <li>Mostrar os dados de contato  do professor(nome, email e localização)</li>
  <li>Mostrar qual a sala do professor solicitado. Fornecendo tambem instruções de onde encontra-lo</li>
  <li>Mostrar horarios do intercampi de todos os campus da UnB</li>
  <li>Manter uma relação interativa e amigável com o usuário.</li>
  <li>Realizar uma conversação com caráter informativo.</li>
 </ul>
</html>

### Principais Tecnologias utilizadas
<ul>
  <li> Rasa Core (Fluxo de conversa) </li>
  <li> Rasa NLU ( Processamento e extração de informações) </li>
  <li> Flask (microframework utilizado para os microserviços) </li>
  <li> MongoDB (NoSQL database) </li>
</ul>
    
    
### Entenda um pouco da arquitetura:
![diagrama de relacoes](./docs/imagens/diagrama-relacoes.png)

## Guia de Contribuição

Para começar o desenvolvimento do ChatBot, é necessário montar as imagens descritas pelos Dockerfiles utilizando a ferramenta docker :

1. Construir imagem do telegram: `sudo cd docker/ && docker build -t telegram-jp:latest -f Telegram.Dockerfile .`
'''

2. Construir a imagem do microserviço que informa o intercampi: `sudo cd docker/ && docker build -t jp-intercampi:latest -f Intercamping.Dockerfile .`
'''

3. Construir a imagem do microserviço que envia uma imagem com o horário de todos os intercampis: `sudo cd docker/ && docker build -t jp-send-pdf:latest -f SendPdf.Dockerfile .`
'''

4. Construir a imagem das ações personalizadas do RASA: `sudo cd.. && docker build -t jp:latest .`
'''

Após montar as imagens necessárias, use o ngrok para ser possivel estabelecer uma conexão com as URL's e o Tino de forma segura por meio de https:

### No diretório onde se encontra seu Ngrok, abra o terminal e execute os seguintes comandos em janelas separadas :

1. `./ngrok http 5000`
'''

2. `./ngrok http 5055`
'''

3. `./ngrok http 5002`
'''

4. `./ngrok http 5003`
'''

### Após executar os comandos acima certifique-se de que os terminais permaneçam abertos e executando o Ngrok
'''

Depois de utilizar o ngrok nas portas necessárias, é preciso alterar as variáveis de ambiente localizadas no arquivo .env :

1. Altere o valor atribuido a variavel 'MONGO_ID' para o nome do conteiner(mongo) ou seu id;
'''
2. Altere o valor atribuido a váriavel 'TELEGRAM_TOKEN' para o token do seu telegram-bot, gerado por meio do BotFather(bot presente no telegram).
'''
3. Nas demais variáveis('..._WEBHOOK') insira os respectivos links referentes as portas correspondentes nos terminais rodando o ngrok. Certifique-se de pegar os links com o 'https://...' nos terminais rodando o ngrok
'''

Ufa! Até que enfim estamos prontos para subir o ChatBot Tino, agora é só executar o docker-compose (necessário docker-compose instalado) para subir os containers (incluindo o banco de dados mongo e o redis):

1. sudo docker-compose up
'''

### Agora sim esta tudo pronto para testar o Tino no Telegram... Manda um oi la !    



