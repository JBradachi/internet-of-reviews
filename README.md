# internet-of-reviews

A reviews and descriptions dataset of smart objects

## Table of Contents

- [internet-of-reviews](#internet-of-reviews)
  - [Table of Contents](#table-of-contents)
  - [Repository Structure](#repository-structure)
  - [Data Structure](#data-structure)
    - [avaliacoes](#avaliacoes)
    - [contexto](#contexto)
    - [perguntas](#perguntas)
    - [produtos](#produtos)

## Repository Structure

A estrutura do repositório é composta por 2 diretórios:

- **src:** Diretório dedicado para os arquivos fonte do projeto. Nele há um arquivo com o código de coleta dos dados, e dois arquivos de tratamento e análise dos dados
- **data:** Diretório dedicado para os arquivos com os dados gerados por esse trabalho. Vale ressaltar que foram disponibilizados no formato CSV para facilitar seu uso.

## Data Structure

Os dados foram estruturados separando por tipo de dado coletado da seguinte forma:

### avaliacoes

As avaliações dos produtos possuem a seguinte estrutura:

- **texto:** dado do tipo string que contém o texto da avaliação.
- **nota:** dado do tipo inteito que contém a nota da avaliação.
- **id:** dado do tipo string que contém o id do produto usado na plataforma do Mercado Livre
- **data:** dado do tipo string que contém a data da postagem da avaliação TODO: tratar

### contexto

- **Context_Id:** dado do tipo string que contém o id da descrição usado na plataforma do Mercado Livre
- **Context:** dado do tipo string que contém o nome da descrição
- **value_id:** dado do tipo inteiro que contém o id do valor usado na plataforma do Mercado Livre
- **value_name:** dado do tipo string que contém o valor
- **id:** dado do tipo string que contém o id do produto usado na plataforma do Mercado Livre

### perguntas

- **pergunta:** dado do tipo string que contém a pergunta do cliente
- **resposta:** dado do tipo string que contém a resposta do vendedor
- **id:** dado do tipo string que contém o id do produto usado na plataforma do Mercado Livre
- **data:** dado do tipo string que contém a data da postagem da pergunta TODO: tratar

### produtos

- **id:** dado do tipo string que contém o id do produto usado na plataforma do Mercado Livre
- **date_created:** dado do tipo string que contém a data de criação do produto
- **catalog_product_id:** dado do tipo string que contém o id do produto no catálogo usado na plataforma do Mercado Livre
- **domain_id:** dado do tipo string que contem o id de domínio do produto.
- **name:** dado do tipo string que contém o nome do produto
- **keywords:** dado do tipo string que contém as palavras chaves do produto.