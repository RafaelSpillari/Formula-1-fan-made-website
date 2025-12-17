F1 Hub — Portal da Fórmula 1 (Temporada 2025)
1. Descrição do Projeto
O F1 Hub é um sistema web desenvolvido no contexto acadêmico com a finalidade de consolidar e demonstrar conhecimentos adquiridos nas áreas de desenvolvimento de software, programação web e banco de dados. O projeto simula um portal informativo dedicado à Fórmula 1, apresentando dados organizados da temporada 2025, como pilotos, equipes, circuitos, calendário de corridas e classificação do campeonato.

A aplicação foi construída utilizando o framework Flask, adotando a linguagem Python como base para o backend, e o banco de dados SQLite para persistência das informações. O sistema segue o padrão arquitetural Model-View-Controller (MVC), garantindo separação entre a lógica de negócio, a camada de apresentação e o acesso aos dados, o que contribui para maior organização, manutenção e escalabilidade do código.

O frontend da aplicação foi desenvolvido com HTML5, CSS3 e Bootstrap 5, proporcionando uma interface responsiva, consistente e inspirada em portais esportivos modernos. A renderização dinâmica das páginas é realizada por meio do motor de templates Jinja2, permitindo a integração eficiente entre os dados armazenados no banco de dados e a interface apresentada ao usuário.

Além do caráter informativo, o sistema implementa funcionalidades essenciais de aplicações web reais, como cadastro e autenticação de usuários, controle de sessões e navegação dinâmica entre páginas. Essas funcionalidades permitem ao estudante aplicar conceitos de segurança básica, como criptografia de senhas e gerenciamento de sessões, reforçando boas práticas de desenvolvimento.

Os dados referentes à temporada 2025 foram inseridos de forma estática, com o objetivo de garantir estabilidade da aplicação e evitar dependência de serviços externos ou APIs de terceiros. Dessa forma, o projeto mantém previsibilidade de funcionamento e facilita sua avaliação e apresentação.

O F1 Hub não possui fins comerciais ou lucrativos, sendo desenvolvido exclusivamente para fins educacionais.

2. Objetivos
Aplicar conceitos de desenvolvimento web utilizando Python e Flask
Implementar persistência de dados com SQLite
Utilizar templates dinâmicos por meio do Jinja2
Desenvolver um sistema de autenticação de usuários
Criar uma interface responsiva e organizada utilizando Bootstrap
Simular o funcionamento de um portal esportivo real
3. Tecnologias Utilizadas
Python 3
Flask
SQLite
HTML5
CSS3
Bootstrap 5
Jinja2
JavaScript (básico)
4. Estrutura do Projeto
f1_fan_site/ │ ├── app.py # Arquivo principal da aplicação Flask ├── site.db # Banco de dados SQLite ├── README.md # Documentação do projeto │ ├── templates/ # Templates HTML (Jinja2) │ ├── base.html │ ├── index.html │ ├── pilotos.html │ ├── driver_detail.html │ ├── equipes.html │ ├── team_detail.html │ ├── circuitos.html │ ├── circuito_detail.html │ ├── classificacao.html │ ├── calendario.html │ ├── login.html │ └── register.html │ ├── static/ │ ├── css/ │ │ └── style.css │ ├── js/ │ │ └── main.js │ └── img/ │ ├── drivers/ │ └── teams/

5. Funcionalidades
5.1 Autenticação
Cadastro de usuários
Login com senha criptografada
Controle de sessão
5.2 Pilotos
Listagem completa de pilotos da temporada 2025
Exibição de pontuação e nacionalidade
Página individual de cada piloto
5.3 Equipes
Classificação das equipes por pontuação
Associação entre equipes e pilotos
Página individual com detalhes da equipe
5.4 Circuitos
Listagem de circuitos da temporada 2025
Exibição das datas das corridas
Página individual para cada circuito
Visualização do calendário completo
5.5 Classificação
Tabela de classificação dos pilotos
Ordenação por pontuação
Destaque visual para os primeiros colocados
6. Como Executar o Projeto
6.1 Pré-requisitos
Python 3 instalado
Navegador web atualizado
6.2 Instalação das dependências
pip install flask werkzeug

### 6.2 Instalação das dependências

python app.py

### 6.4
Após a execução, o sistema pode ser acessado pelo endereço:

http://localhost:8000

O banco de dados é criado automaticamente na primeira execução da aplicação.

7. Observações

Dados consolidados da Fórmula 1

Estatísticas gerais inspiradas no site oficial da F1

Calendário baseado na temporada atual

Observação: valores podem ser ajustados para fins acadêmicos.

O projeto possui finalidade exclusivamente acadêmica.

O layout foi desenvolvido com inspiração em portais esportivos modernos, sem reutilização de conteúdo proprietário.

8. Conceitos Aplicados

Arquitetura MVC
CRUD com SQLite
Templates dinâmicos com Jinja2
Autenticação e sessões
Organização de projetos web
Boas práticas de desenvolvimento

# Atualizações
    O projeto será atualizado, em próximas versões, para comportar outro pilotos históricos como Senna, Prost, Lauda e etc. Além disso podemos adicionar fotos de carros especiais, uma aba dentro do card de cada piloto para capacetes, recordes. Esse é um projeto contínuo, que deve ser atualizado quando novas ideias, conhecimento de ferramentas e novad empolgantes temporadas de formula 1 surgurirem, ou até mesmo temporadas passadas sejam revisitadas...

    
9. Autor

Rafael Spillari
Projeto acadêmico — Curso de Ciencias da computação 
Ano: 2025.
