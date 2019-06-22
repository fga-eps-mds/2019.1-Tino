# Histórico de Revisão

| Data   | Versão | Modificação  | Autor  |
| :------- | :--------- | :---------------- | :------- |
| 02/04/2019 | 0.1   |  Criação de todos os tópicos do documento  |  Lucas Leite, Lucas Lopes, Luís Bruno, Luiz Gustavo |
| 12/04/2019 | 0.2   | Definição das tecnologias e arquitetura  | Lucas Leite  |
| 24/04/2019 | 0.3   | Adição de mais tópicos  | MDS(Todos)  |
| 07/05/2019 | 0.4   | Modificação da parte de representação da arquitetura| Luis Bruno, Lucas Leite e Luiz Gustavo |
| 02/06/2019 | 0.5   | Modificação Introdução e topico de tecnologias usadas | Luiz Gustavo e Lucas Leite |



# 1. Introdução 
<p  align="justify">Este documento tem como objetivo apresentar de forma abrangente a arquitetura do sistema do ChatBot Tino.</p> 

## 1.1 Finalidade  

<p  align="justify">Este documento fornece uma visão arquitetural abrangente do sistema, usando diversas visões de arquitetura para representar diferentes aspectos do sistema. Seu objetivo é captar e transmitir as decisões arquiteturais significativas que foram feitas no sistema.</p>

## 1.2 Escopo

<p  align="justify">Este documento se aplica ao ChatBot Tino, um sistema que será desenvolvido por alunos das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software, da Universidade de Brasília - campus Gama. </p>

## 1.3 Definições, Acrônimos e Abreviações

<html>
<ul>
<li> FGA: Faculdade do Gama - <i>Campus da Universidade de Brasília localizado no Gama.</i></li>
<li> MDS: <i>Método de Desenvolvimento de Software</i></li>
<li> API: <i>Application Programming Interface </i></li>
<li> UnB: <i>Universidade de Brasília</i></li>
<li> Tino: <i>Nome do ChatBot</i>  </li>
<li> ChatBot: <i> Programa de computador capaz de conduzir uma conversação através de via auditiva ou texto</i> </li>

</ul>
</html>

## 1.4 Visão Geral

<p  align="justify">O documento, através de dez principais tópicos e suas ramificações, visa detalhar a arquitetura e os requisitos do software do projeto. Tendo como objetivo facilitar o desenvolvimento e esclarecendo dúvidas a respeito deste. </p>

Estrutura do documento:  

<html>
<ul>

<li> Introdução; </li>
<li> Representação da Arquitetura; </li>
<li> Metas e Restrições de Arquitetura; </li>
<li> Visão Lógica </li>


</ul>
</html>

## 1.5 Referências



> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.

> RODRIGUES, Pedro; BLANCO, Matheus; BRAGA, Gabriel; FILA herme; DE SOUZA, Letícia. <b>Lino:</b> Documento de Arquitetura. Disponível em:
<https://github.com/fga-eps-mds/2018.2-Lino/docs/>.




# 2. Representação da Arquitetura


![diagrama de relacoes](./imagens/diagrama-relacoes.png)

<p  align="justify">A representação da arquitetura é representada pelo diagrama acima, iniciando-se no usuário.</p>
<p  align="justify">Ao enviar uma mensagem, por meio das aplicações do Telegram e Facebook Messenger, ela é passada pelos webhooks (há um webhook para cada aplicação), que é a forma de envio de informações entre dois sistemas. Lá, tem-se os dados dessa mensagem, tais como o id do usuário que enviou, a data e a mensagem em si. Esses dados são salvos no Mongo, na coleção Usuários.</p>
<p  align="justify">Após isso, a mensagem já pode ser processada pelo Rasa. O Rasa NLU faz a detecção da intenção da mensagem recebida, enquanto o Rasa Core faz a escolha da melhor resposta a ser enviada para o usuário (mais detalhes na próxima seção do documento).</p>

<p align="justify">Após a seleção da melhor resposta a ser enviada é analisado se essa resposta pode ser diretamente enviada ao usuário e então encerrar o fluxo, ou se deve chamar uma ação personalizada, onde terá acesso ao banco de dados.</p>
<p align="justify">Dependendo da ação personalizada, será chamado um microservice que faz um acesso ao Mongo na coleção específica. Sendo o microservice de Intercampi, será acessado no Mongo a coleção de Intercampi, sendo o microservice de Professor, a coleção acessada no Mongo é a Professor. A informação é retornada e tratada e então enviada ao usuário.</p>


## 2.1  Tecnologias escolhidas - Rasa Core e Rasa NLU
<p align="justify">O Rasa é um framework para construir softwares de conversação: bots Messenger / Slack, skills de Alexa. Foi a tecnologia que mais atendeu às necessidades da equipe.</p>
<p align="justify">O desenvolvimento de um diálogo interativo com o usuário é de grande importância para o contexto do bot, através da característica de Machine Learning para a melhora de suas conversas, é possível manter um diálogo apropriado e flexível de acordo com as intenções do usuário.</p>
<p align="justify">Dentro da arquitetura do Bot, o Rasa Core é um dos componentes principais, permitindo o treinamento de estórias de usuário e a criação de um modelo treinado. Em associação ao Rasa Core, existe outro componente tecnológico fundamental na arquitetura do ChatBot: Rasa NLU, este trabalha com o processamento natural de linguagem e, a partir dela, o desenvolvedor abre portas relacionadas ao processamento de texto que o permitem criar um ambiente de comunicação mais interativo e humano, possibilitando assim a criação de uma comunicação mais fluida e dinâmica com o usuário.</p>
<p align="justify">A utilização das ferramentas proporcionadas pelo Framework Rasa nos permitem uma interação mais humanizada com o usuário, possibilitando também,depois de algumas interações com usuários, um auto-treinamento para melhor se comunicar com o exterior. Este é o principal objetivo da utilização do Rasa NLU para o processamento de linguagem. Alguns benefícios do Framework são:</p>
<html>
<li>- Rasa usa aprendizado  de máquina treinando em conversas de exemplos;</li>
<li>- A plataforma Rasa é Open source e customizável para o panorama do projeto;</li>
<li>- Manuseio de conversação com deep learning para auto-evolução;</li>
</html>


### 2.1.1 Telegram

<p align="justify">O Telegram é um aplicativo de troca de mensagens, utilizado para bate-papo. O telegram possibilita aos desenvolvedores implementação de funcionaliades e bots, através da sua API.</p>

### 2.1.2 Mongo DB

<p align="justify">O MongoDB é um banco de dados orientado a documentos (document database) no formato JSON. A API se conectará com o banco, assim enviando os dados fornecidos pelas interações feitas no chatbot e também recebendo as informações necessárias armazenadas no banco de dados.</p>


### 2.1.3 Flask
<p align="justify">O Flask é um micro-framework desenvolvido em python baseado em 2 principais pontos:
WerkZeug é uma biblioteca para desenvolvimento de apps WSGI que é a especificação universal de como deve ser a interface entre um app Python e um web server. Ela possui a implementação básica deste padrão para interceptar requests e lidar com response, controle de cache, cookies, status HTTP, roteamento de urls e também conta com uma poderosa ferramenta de debug. </p>

### 2.1.4 Jinja2
<p align="justify">O Jinja2 é um template engine escrito em Python e se encarrega de renderizar este template, ou seja, ele substitui os placeholders pelo valor de suas variáveis.</p>

### 2.1.5 Ngrok
<p align="justify">Devido a necessidade da utilização de uma conexão segura servindo de WebHook para o Telegram, utilizamos um pequeno software de linha de comando que nos permite criar um túnel a partir do localhost do desenvolvedor, podendo assim serem utilizados métodos http em uma url web normal que se conecta com o localhost.</p>

## 2.2 Serviços Externos

### 2.2.1 API Telegram Messenger

<p  align="justify"><i>Telegram Messenger</i> é um aplicativo de comunicação baseado em nuvem. O qual oferece a possibilidade para seus usuários desenvolvedores criarem <i>bots</i> a partir de sua API.</p>

<p  align="justify">Essa <i>API</i> será a ponte de comunicação com o usuário. O código fonte será implementado e o Ludum irá interagir com o usuário de acordo com o que foi definido neste código fonte.</p>

### 2.2.2 Microserviço(API em Flask) Intercampi

<p align="justify">Serviço de API  utilizando Flask para fornecer os dados atualizados acerca da tabela do Intercampi disponível no site da UnB.</p>

### 2.2.3 Microserviço(API em Flask) Send-pdf

<p align="justify">Serviço de API  utilizando Flask para o envio de imagens com os dados de todas as linhas de Intercampi disponíveis,enviando uma imagem com uma tabela contendo todas a linhas disponiveis.</p>

### 2.2.4 Serviço para popular o banco com os dados dos professores

<p align="justify">Script em python que tem a finalidade de ler o csv pronto com os dados dos professores e popular o banco com esses dados, jogando todos os dados de determinado professor em um document dentro de uma collection.</p>

# 3. Metas e Restrições de Arquitetura
<html>
<ul>
<li>Utilização de um Banco de Dados MongoDB para cada serviço interno, logo um banco referente ao serviço de informações a respeito dos professores e seus respectivos horários e locais de atendimento, um banco para o serviço de horários de chegada e saída do intercampi, um banco para o serviço de documentação necessária para o estágio obrigatório e um banco para cada serviço de mensagem que vamos utilizar (Facebook Messenger e Telegram Messenger);</li>
<li>Disponibilizar o sistema a maior quantidade de tempo possível, reconhecendo as limitações dos servidores utilizados para hospedagem do Bot.</li>
<li> O núcleo do Tino deve ser desenvolvido em Pyhton 3.6 </i>
<li> Uso do Docker para desenvolvimento em ambientes isolados; </li>
<li> Necessidade de conexão com a internet</li>
<li> O Tino deve ser desenvolvido no prazo de um semestre letivo da UnB; </li>
<li>As metas do projeto são disponibilizar um fluxo de conversa com o usuário a fim de atender/suprir as dúvidas em relação à procedimentos voltados restritamente à comunidade acadêmica, especificamente do Campus UnB-Gama;</li>

</ul>
</html>


# 4. Visão Lógica

## 4.1 Diagrama de Pacotes

<p align="justify">Neste tópico se encontra o diagrama de pacotes, bem como a explicação referente a suas utilidades.</p>
<html>
<ul>
<li>O Pacote 2019.1-Tino é o pacote principal do projeto e contém todos os outros sub-pacotes e documentos disponíveis no projeto.</li>
<li>No Pacote docs, no interior de 2019.1-Tino, estão contidos os documentos de visão e de arquitetura para melhor compreesão dos detalhes acerca da proposta.</li>
<li>O Pacote microservices contém todos os microsserviços externos relacionados à arquitetura do Bot.</li>
<li>O Pacote csv contém o arquivo CSV com todos os dados dos professores e coordenadores, que é atualizado manualmente, utilizado pelo microservice de professor para a atualização dos dados dos professores no banco de dados. O nome do arquivo .csv deve ser professores.csv</li>    
</ul>
</html>

# 5. Tamanho e Desempenho


<p align="justify"> Como o Tino é um ChatBot para o telegram, seu tamanho tende a seguir um padrão visto em aplicações semelhantes utilizando a tecnologia Rasa.Devido a utilização de microsserviços temos como resultado um aumento significativo de sua robustez.</p>
<p align="justify"> No que tange o desempenho da aplicação como um todo,a arquitetura baseada em microserviços possui grande autonomia entre suas partes, devido a isso, caso haja falha em alguns dos microserviços envolvidos, não há o compromentimento total do ChatBot. Porém, o correto funcionamento do Tino depende de questões que envolvem os serviços externos, como por exemplo o serviço que fornece as linhas do intercampi e seus horarios, sendo então fundamental o correto funcionamento dos serviços externos para o cumprimento de todas as suas funções de forma adequada a proposta.</p>

