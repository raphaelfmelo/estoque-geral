# 📁 Estoque Prático

Sistema de gerenciamento de estoque desenvolvido utilizando Streamlit como interface e SQLite como banco de dados.

O projeto foi desenvolvido como estudo prático de programação, banco de dados e desenvolvimento de uma aplicação funcional para gerenciamento de produtos e movimentações de estoque.

---

## 🛠️ Tecnologias

* Python
* Streamlit
* SQLite
* Pandas
* Git
* GitHub

---

## ⚙️ Funcionalidades

* Dashboard com visão geral do estoque
* Cadastro de produtos
* Edição de produtos
* Desativação de produtos
* Reativação de produtos
* Registro de entrada e saída de estoque
* Histórico de movimentações
* Controle de estoque mínimo
* Validação de produtos e movimentações

---

## 📁 Estrutura do Projeto

* `app.py` - tela inicial e dashboard
* `estoque_inicial.db` - banco de dados SQLite inicial
* `funcoesCRUD.py`
* `funcoesMOVES.py`
* `README.md`
* `requirements.txt`
* `pages/`

  * `1_Produtos.py`
  * `2_Movimentacoes.py`
  * `3_Historico.py`

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/raphaelfmelo/Projeto-Estoque.git
cd Projeto-Estoque
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**No Windows:**

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure o banco de dados

O projeto utiliza SQLite. O arquivo `estoque_inicial.db`, contendo a estrutura inicial do banco de dados, já está incluído no projeto.

As tabelas utilizadas são:

* `produtos`
* `movimentacoes`

A tabela `movimentacoes` possui uma chave estrangeira relacionada à tabela `produtos`.

Não é necessário realizar nenhuma configuração adicional no banco de dados.

### 6. Execute o sistema

```bash
streamlit run app.py
```

O Streamlit disponibilizará a aplicação no navegador.

---

## 🗄️ Banco de dados

O projeto utiliza SQLite. Um banco de dados inicial vazio, chamado `estoque_inicial.db`, é disponibilizado junto ao projeto.

O arquivo contém a estrutura necessária para o funcionamento do sistema e é disponibilizado inicialmente sem registros de produtos ou movimentações.

O banco possui as tabelas:

* `produtos`
* `movimentacoes`

A tabela `movimentacoes` possui uma chave estrangeira relacionada à tabela `produtos`.

Não é necessário criar um banco de dados manualmente. Basta manter o arquivo `estoque_inicial.db` na pasta do projeto.

---

## 📌 Sobre o Projeto

O programa foi desenvolvido como um projeto de prática e portfólio, com foco na construção de uma aplicação de gerenciamento de estoque utilizando Python.

Durante o desenvolvimento foram praticados os seguintes conceitos:

* Funções e modularização
* CRUD
* SQL
* SQLite
* Chaves estrangeiras
* Validação de dados
* Controle de estoque
* Ativação e desativação de registros
* Manipulação de dados com Pandas
* Desenvolvimento de interfaces com Streamlit
* Organização de projetos
* Git e GitHub
