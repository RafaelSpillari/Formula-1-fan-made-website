# 🏎️ F1 Hub — Portal da Fórmula 1 (Temporada 2025)

## 1. Descrição do Projeto

O **F1 Hub** é um sistema web desenvolvido em contexto acadêmico com a finalidade de consolidar e demonstrar conhecimentos adquiridos nas áreas de **desenvolvimento de software, programação web e banco de dados**.

O projeto simula um **portal informativo dedicado à Fórmula 1**, apresentando dados organizados da **temporada 2025**, como:
- Pilotos
- Equipes
- Circuitos
- Calendário de corridas
- Classificação do campeonato

A aplicação foi construída utilizando o **framework Flask**, com **Python** no backend e **SQLite** para persistência de dados. O sistema segue o padrão arquitetural **Model-View-Controller (MVC)**, garantindo separação entre lógica de negócio, camada de apresentação e acesso aos dados, o que contribui para maior organização, manutenção e escalabilidade do código.

O frontend foi desenvolvido com **HTML5, CSS3 e Bootstrap 5**, proporcionando uma interface **responsiva, consistente e moderna**, inspirada em portais esportivos oficiais. A renderização dinâmica das páginas é realizada por meio do motor de templates **Jinja2**, permitindo integração eficiente entre os dados armazenados e a interface exibida ao usuário.

Além do caráter informativo, o sistema implementa funcionalidades essenciais de aplicações web reais, como:
- Cadastro e autenticação de usuários
- Controle de sessões
- Navegação dinâmica entre páginas

Essas funcionalidades permitem a aplicação de conceitos de **segurança básica**, como criptografia de senhas e gerenciamento de sessões, reforçando boas práticas de desenvolvimento.

Os dados referentes à temporada 2025 foram inseridos de forma **estática**, garantindo estabilidade da aplicação e evitando dependência de serviços externos ou APIs de terceiros, o que facilita sua avaliação e apresentação.

> O **F1 Hub não possui fins comerciais**, sendo desenvolvido exclusivamente para fins educacionais.

---

## 2. Objetivos

- Aplicar conceitos de desenvolvimento web utilizando **Python e Flask**
- Implementar persistência de dados com **SQLite**
- Utilizar templates dinâmicos com **Jinja2**
- Desenvolver um sistema de **autenticação de usuários**
- Criar uma interface responsiva e organizada com **Bootstrap**
- Simular o funcionamento de um **portal esportivo real**

---

## 3. Tecnologias Utilizadas

- Python 3  
- Flask  
- SQLite  
- HTML5  
- CSS3  
- Bootstrap 5  
- Jinja2  
- JavaScript (básico)

---

## 4. Estrutura do Projeto

f1_fan_site/
│
├── app.py # Arquivo principal da aplicação Flask
├── site.db # Banco de dados SQLite
├── README.md # Documentação do projeto
│
├── templates/ # Templates HTML (Jinja2)
│ ├── base.html
│ ├── index.html
│ ├── pilotos.html
│ ├── driver_detail.html
│ ├── equipes.html
│ ├── team_detail.html
│ ├── circuitos.html
│ ├── circuito_detail.html
│ ├── classificacao.html
│ ├── calendario.html
│ ├── login.html
│ └── register.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── main.js
│ └── img/
│ ├── drivers/
│ └── teams/

---

## 5. Funcionalidades

### 5.1 Autenticação
- Cadastro de usuários
- Login com senha criptografada
- Controle de sessão

### 5.2 Pilotos
- Listagem completa dos pilotos da temporada 2025
- Exibição de pontuação e nacionalidade
- Página individual com estatísticas de carreira

### 5.3 Equipes
- Classificação das equipes por pontuação
- Associação entre equipes e pilotos
- Página individual com detalhes da equipe

### 5.4 Circuitos
- Listagem dos circuitos da temporada 2025
- Exibição das datas das corridas
- Página individual de cada circuito
- Visualização do calendário completo

### 5.5 Classificação
- Tabela de classificação dos pilotos
- Ordenação automática por pontuação
- Destaque visual para os primeiros colocados

---

## 6. Como Executar o Projeto

### 6.1 Pré-requisitos
- Python 3 instalado
- Navegador web atualizado

### 6.2 Instalação das Dependências

pip install flask werkzeug

### 6.3 Execução do Projeto

python app.py

### 6.4 Acesso

Após a execução, a aplicação estará disponível em:

http://localhost:8000


### 7. Observações

Dados consolidados da Fórmula 1

Estatísticas inspiradas no site oficial da F1

Calendário baseado na temporada atual

Valores podem ser ajustados para fins acadêmicos

O layout foi desenvolvido com inspiração em portais esportivos modernos, sem reutilização de conteúdo proprietário.

### 8. Conceitos Aplicados

Arquitetura MVC

CRUD com SQLite

Templates dinâmicos com Jinja2

Autenticação e sessões

Organização de projetos web

Boas práticas de desenvolvimento

### 🔄 Atualizações Futuras

O projeto será atualizado em versões futuras para:

Inclusão de pilotos históricos (Senna, Prost, Lauda, entre outros)

Adição de fotos de carros especiais

Seção dedicada a capacetes, recordes e estatísticas avançadas

Expansão para temporadas passadas

O F1 Hub é um projeto contínuo, que evoluirá conforme novas ideias, aprendizados e temporadas marcantes da Fórmula 1.

### 9. Autor

Rafael Spillari

Projeto Acadêmico — Curso de Ciência da Computação

Ano: 2025
