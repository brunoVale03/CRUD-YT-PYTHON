# YouTube URL Manager - Back-end (Django)

Este projeto é o Back-end de uma aplicação CRUD para gerenciamento de URLs do YouTube, desenvolvido em **Django** e utilizando o **Django REST Framework** para expor uma API que interage com o banco de dados.

## Funcionalidades

O Back-end oferece as seguintes funcionalidades via API RESTful:

- **Inserir uma URL do YouTube:** Adiciona uma nova URL ao banco de dados.
- **Listar URLs do YouTube:** Retorna todas as URLs armazenadas no sistema.
- **Recuperar uma URL específica:** Retorna os dados de uma URL armazenada.
- **Deletar uma URL:** Remove uma URL do banco de dados.

---

## Tecnologias Utilizadas

- **Django**: Framework web em Python utilizado para gerenciar o Back-end da aplicação.
- **Django REST Framework (DRF)**: Extensão do Django para criação de APIs RESTful.
- **SQLite**: Banco de dados utilizado para armazenar as URLs (pode ser substituído por outro banco de dados).
- **Python 3.x**: Linguagem de programação para desenvolvimento do Back-end.

---

## Pré-requisitos

Antes de executar o projeto, você precisará ter instalado em sua máquina:
- **Python 3.x**
- **Pip** (gerenciador de pacotes Python)
- **Virtualenv** (opcional, mas recomendado para isolamento do ambiente)

---

## Instalação e Configuração

### 1. Clonar o Repositório
Clone o repositório do projeto em sua máquina local.

```bash
git clone https://github.com/seu-usuario/youtube-url-manager-backend.git
cd youtube-url-manager-backend
