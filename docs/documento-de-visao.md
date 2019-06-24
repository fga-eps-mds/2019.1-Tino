| Data   | Versão | Modificação  | Autor  |
| :------- | :--------- | :---------------- | :------- |
| 26/03/2019 | 0.1   |  Criação de todos os tópicos do documento  |  Lucas Leite, Lucas Lopes, Luís Bruno, Luiz Gustavo |
| 30/04/2019 | 0.2   | Finalizando perfis envolvidos  | Luis Bruno e Lucas Leite  |
| 30/04/2019 | 0.3   | Finalizando Tópico 9 | MDS(Todos)  |
| 07/05/2019 | 0.4   | Diminuição de escopo| Luis Bruno, Lucas Leite e Luiz Gustavo |

# 1. Introdução

<p align = "justify">Neste documento serão definidas as necessidades, razões e motivações que compõem o escopo do projeto, bem como os propósitos para realização do mesmo. O objetivo deste documento de visão é reduzir riscos que circundam a criação do produto de modo a estabelecer expectativas e proteger as partes envolvidas no desenvolvimento do projeto.</p>

## 1.1 Propósito

<p align = "justify">Este documento tem, por finalidade, estabelecer de modo amplo uma visão geral a respeito da criação de um novo ChatBot destinado aos alunos da Universidade de Brasília - UnB-FGA de maneira a definir as características e utilidades de cada funcionalidade e também o propósito e contexto nas quais se inserem, deixando claro assim sua proposta e peculiaridades.</p>

## 1.2 Escopo

<p align = "justify">O objetivo deste projeto é desenvolver soluções tecnológicas que auxiliem os alunos da Universidade de Brasília- UnB-Fga na utilização dos recursos disponibilizados na faculdade UnB-FGA por meio de um ChatBot. </p>
<p align = "justify">A proposta a ser realizada pela equipe , composta por alunos de EPS e MDS , tem como objetivo  auxiliar por meio de funcionalidades, trazendo dados e informações relevantes, o aluno que deseja facilitar a execução de ações como: Agendamento de horário com professor,obtenção de informações a respeito de contato e localização de professores,obtenção de informações a respeito do intercampi e seus horários de funcionamento.</p>

## 1.3 Definições, acrônimos e abreviações

| Sigla | Definição |
| :--:|:------------------------:|
| UnB | Universidade de Brasília |
| FGA | Faculdade do Gama |
| MDS | Métodos de desenvolvimento de software |
| EPS | Engenharia do Produto de Software |
| Tino | Nome do ChatBot |
| ChatBot |  Programa de computador capaz de conduzir uma conversação através de via auditiva ou texto |
| RU |  Restaurante Universitário|

## 1.4 Referências

<p>https://github.com/fga-eps-mds/2018.2-Lino/blob/master/docs/documento-de-visao.md</p>
<p>https://fga-eps-mds.github.io/2018.2-ComexStat/docs/docVisao</p>


## 1.5 Visão geral

<p align = "justify">Este documento descreve os detalhes sobre as características do ChatBot Tino, especificando os problemas que estimularam a criação dessa solução em software. O documento se divide de maneira a separar as especificações e descrever as mesmas.</p>

# 2.  Posicionando

## 2.1 Oportunidade de Negócios

<p align = "justify">Para obter informações, é preciso ir até a secretaria da universidade ou falar com o coordenador do curso. Por muitas vezes a secretaria está fechada ou o coordenador ausente. Além disso, o aluno tem que ir em horários fixos para obtenção de informações e documentos. 
Com o chatbot, se tornaria mais ágil, podendo obter informações e documentos a qualquer hora do dia e qualquer dia da semana. Também, seria mais cômodo para os servidores da universidade.
.</p>

## 2.2 Descrição do Problema

<table> 
<tr><th>Problema de</th><td> Informações sobre áreas específicas da UnB. Como horário de partida e chegada do intercampi. </td></tr>
<tr><th>Afeta</th><td>Estudantes da Universidade de Brasília</td></tr>
<tr><th>Cujo Impacto é</th><td>Pouca informação sobre processos relacionados a Universidade de Brasília. Assim, causando transtorno para os alunos. </td></tr>
<tr><th>Uma boa solução seria</th><td>Um chatbot capaz de responder e ajudar as principais dúvidas aos alunos. Mais comodidade e agilidade.</td></tr>
</table>

## 2.3 Instrução de Posição do Produto

<table> 
<tr><th>Para</th><td>Universidade de Brasilia - Campus do Gama.</td></tr>
<tr><th>Que</th><td>Queira agilizar e melhorar o processo de obtenção de dados e informações</td></tr>
<tr><th>O(nome do produto)</th><td>Tino</td></tr>
<tr><th>Que</th><td>Tem o objetivo de facilitar a obtenção de informações a respeito de assuntos universitários( horários dos intercampis e dados sobre professor).</td></tr>
</table>

# 3. Descrição dos Envolvidos e dos Usuários

<p align = "justify">Os envolvidos no projeto são os alunos das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software e seus respectivos orientadores, monitores e coaches. O perfil dos envolvidos representa adequadamente os usuários, já que estes entendem as necessidades de grande parte deste público-alvo.
O público-alvo do ChatBot são alunos e, possivelmente, funcionários da FGA.</p>

## 3.1 Resumo dos envolvidos

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Equipe de desenvolvimento de software|Estudantes da Disciplina Métodos de Desenvolvimento de Software.|Desenvolvimento e Testes do Software descrito no documento.|
|Equipe de engenharia de produto de software|Estudantes da Disciplina Engenharia de Produto de Software.|Gestão da Equipe de Desenvolvimento,  arquitetar sistema e automatizar processos.|
|Orientador|Professoras da Universidade de Brasília no campus Faculdade Gama (FGA - UnB) das disciplinas Métodos de Desenvolvimento de Software e Engenharia de Produto de Software.|Orientar as equipe de desenvolvimento e gestão em eventuais dúvidas.|

## 3.2 Resumo dos Usuários

| Nome | Descrição | Responsabilidades |
|:----:|:---------:|:-----------------:|
|Alunos e Funcionários|Participantes da universidade, sejam alunos ou funcionários interessados em obter informações sobre professores ou dados do intercampi|Interação com o ChatBot quando necessário, a fim de sancionar dúvidas e obter informações|

## 3.3 Perfil dos envolvidos


### 3.3.1 Equipe de desenvolvimento de software (MDS)

<table> 
<tr><th>Perfil</th><td>--</td></tr>
<tr><th>Representantes</th><td>Eduardo Cerqueira, Lucas Leite, Lucas Lopes, Luis Bruno, Luiz Gustavo</td></tr>
<tr><th>Descrição</th><td>Desenvolvimento de Software.</td></tr>
<tr><th>Tipo</th><td>Alunos da disciplina Métodos de Desenvolvimento de Software da Universidade de Brasília.</td></tr>
<tr><th>Responsabilidades</th><td>Desenvolver, testar e implantar o software.</td></tr>
<tr><th>Critérios de Sucesso</th><td>Finalizar o desenvolvimento e realizar a entrega do bot no tempo previamente estipulado.</td></tr>
<tr><th>Envolvimento</th><td>Alto.</td></tr>
<tr><th>Problemas/comentários</th><td>Inexperiência da equipe com as principais tecnologias utilizadas para o desenvolvimento na fase inicial do projeto.</td></tr>
</table>

### 3.3.2 Equipe de engenharia de produto de software (EPS)

<table> 
<tr><th>Representantes</th><td>João Pedro e Henrique Lopes Dutra</td></tr>
<tr><th>Descrição</th><td>Gerenciamento do Projeto.</td></tr>
<tr><th>Tipo</th><td>Alunos da disciplina Engenharia de Produto de Software da Universidade de Brasília</td></tr>
<tr><th>Responsabilidades</th><td>Gestão da equipe de desenvolvimento, arquitetar sistema e automatizar processos.</td></tr>
<tr><th>Critérios de Aceitação</th><td>Gerir, orientar e preparar a equipe de desenvolvimento </td></tr>
<tr><th>Envolvimento</th><td>Alto</td></tr>
<tr><th>Problemas/comentários</th><td>Organizar prazos e metas de acordo com o tempo disponível</td></tr>
</table>

### 3.3.3 Orientadores

<table> 
<tr><th>Representantes</th><td>Carla Rocha Rocha e Bruna Nayara Moreira</td></tr>
<tr><th>Tipo</th><td>Professoras da Universidade de Brasília campus Gama das disciplinas MDS e EPS</td></tr>
<tr><th>Responsabilidades</th><td>Orientar, avaliar e sancionar dúvidas das equipes de desenvolvimento e gestão.</td></tr>
<tr><th>Critérios de Aceitação</th><td>Orientar e observar o sucesso dos estudantes no desenvolvimento do software </td></tr>
<tr><th>Envolvimento</th><td>Médio</td></tr>
</table>

## 3.4 Perfil do Usuário

### 3.4.1 Alunos e Funcionários

<table> 
<tr><th>Representantes</th><td>Alunos e funcionários da Universidade de Brasília, campus Gama.</td></tr>
<tr><th>Descrição</th><td>Parte da comunidade que possui dúvidas acerca de algo referente à Universidade de Brasília, campus Gama.</td></tr>
<tr><th>Tipo</th><td>Alunos da universidade e Funcionários.</td></tr>
<tr><th>Responsabilidades</th><td>Interação com o ChatBot quando necessário, a fim de sancionar dúvidas e obter informações.
</td></tr>
<tr><th>Critérios de Aceitação</th><td>Dúvidas e informações esclarecidas com sucesso pelo ChatBot, via Telegram.</td></tr>
<tr><th>Envolvimento</th><td>Alto</td></tr>
<tr><th>Problemas/comentários</th><td>O número de usuários cadastrados no Telegram é muito inferior quando comparados com outras plataformas de comunicação, porém essas outras aplicações não suportam a implantação de ChatBot ou necessitam de outros recursos para tal finalidade (Ex.: WhatsApp, Instagram).</td></tr>
</table>

## 3.5 Principais Necessidades da Parte Interessada ou do Usuário

| Necessidade| Prioridade | Solução Atual| Solução proposta | 
|:----:|:---------:|:-----------------:|:------------------:|
|Obter informações sobre os horários do Intercampi.|Alta| Buscar tais informações no site da UnB ou em painéis informativos espalhados pela universidade| Interagir com o ChatBot e questionar sobre os horários do intercampi ou o próximo intercampi que irá sair, que pode ser feito pelo dispositivo móvel.| Obter informações sobre contato e sala dos professores e marcar horário de atendimento na sua agenda pessoal|Alta| Buscar tais informações no site da UnB ou em painéis informativos espalhados pela universidade| Interagir com o ChatBot e questionar sobre contato e/ou localização de algum professor|

## 3.6 Alternativas e Concorrência  

<p align = "justify">Não existem.</p>

# 4. Visão Geral do Produto

## 4.1 Perspectiva do Produto  

<p align = "justify">O ChatBot Tino possui como objetivo principal prover soluções tecnológicas eficazes para melhor utilização dos serviços disponibilizados pela UnB e também uma facilitação na obtenção de dados úteis aos alunos.Visto isso,temos o serviço de transporte Intercampi, que , por meio do ChatBot terá sua  utilização aprimorada visando emitir alertas e informações úteis a respeito de horários.Contando  com informações disponíveis no site da instituição , serão automatizadas tarefas do secretariado, emitindo assim informações importantes de modo eficiente e possibilitando recursos de agendamento de horário.</p>

## 4.2 Resumo dos Recursos

| Benefício para o cliente | Recursos de suporte |
|:------------------------:|:-------------------:|
|Fornece informações e avisos sobre o Intercampi e seus horários de forma fácil e rápida. |O ChatBot faz uso de dados presentes no site da instituição e em painéis informativos da faculdade para obter as informações necessárias visando facilitar a visualização dos horários.|
| Facilita o contato direto ou indireto do aluno com o professor |O ChatBot, quando questionado a respeito de um professor específico, fornece para o usuário informações úteis a respeito de contato e localização do mesmo, utilizando para isso informações provindas do site da UnB e um mecanismo de agendamento para encontro. |
| Interação entre usuario e ChatBot .| Por meio de uma interação descontraída e com intuito informativo,o ChatBot conduz a conversação de forma a facilitar os anseios do usuário |


# 5. Recursos do Produto

O ChatBot Tino é capaz de:

<html>
<ul>
<li>Mostrar os dados de contato  do professor(nome, email e localização)</li>
<li>Mostrar qual a sala do professor solicitado. Fornecendo tambem instruções de onde encontra-lo</li>
<li>Mostrar horarios do intercampi de todos os campus da UnB</li>
<li>Manter uma relação interativa e amigável com o usuário.</li>
<li>Realizar uma conversação com caráter informativo.</li>

</ul>
</html>

# 6. Restrições
</p align = "justify">Listagem de restrições externas e outras dependências:</p>

<html>
<ul>
<li>Conexão com a Internet</li>
<li>Telegram</li>
<li>Foco para aprender novas tecnologias</li>
<li>Prazo para finalização do projeto: 25/06/2019.</li>
</ul>
</html>


## 6.1 Restrições de confiabilidade

<p align = "justify">O sistema deverá ter cobertura de testes </p>

# 7. Faixas de Qualidade

## 7.1 Requisitos do Sistema

<p align = "justify">A aplicação é compatível com todos os sistemas em que o Telegram é compatível..</p>
<p align = "justify">Telegram - Android (versão 4.1 e superior), iPhone/iPad (versão 6 e superior), Windows Phone, Linux, Windows, MacOs e Web (navegador).</p>


## 7.2 Requisitos de Design

<p align = "justify">A aplicação é auto explicativa de forma que, para obter os resultados e informações desejadas, o usuário deve interagir com o ChatBot da mesma forma que interage com um usuário comum nas plataformas. Além disso, o ChatBot colabora com a experiência do usuário dando dicas de possíveis perguntas/opções e suas funcionalidades.</p>

# 8. Outros requisitos do produto

## 8.1 Requisitos do sistema

<p align = "justify">A aplicação deverá ser acessada por dispositivos que possuem compatibilidade com Telegram.</p>

## 8.2 Requisitos de desempenho

<p align = "justify"> No que se refere a requisitos de desempenho o usuário deve possuir uma conexão estável com a internet que lhe possibilite o acesso ao Telegram, plataforma que faz a interação com o ChatBot.</p>

## 9.4 Requisitos Ambientais

<p align="justify">A aplicação não possui requisitos ambientais referentes a hardware e software que possam ser considerados, visto que se trata de um software sem interação ambiental direta e que possui uma interação rápida e prática com o usuário. </p>









