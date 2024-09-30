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
- **Python 3.11**: Linguagem de programação para desenvolvimento do Back-end.

---

## Pré-requisitos

Antes de executar o projeto, você precisará ter instalado em sua máquina:
- **Python 3.11**
- **Pip** (gerenciador de pacotes Python)
- **Virtualenv** (opcional, mas recomendado para isolamento do ambiente)

---

## Instalação e Configuração

### 1. Clonar o Repositório
Clone o repositório do projeto em sua máquina local.

```bash
git clone https://github.com/brunoVale03/youtube-url-manager-backend.git
cd youtube-url-manager-backend
```

### 2. Criar e Ativar o Ambiente Virtual

É recomendável criar um ambiente virtual para instalar as dependências do projeto:

```bash

python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale as bibliotecas e pacotes necessários:

```bash

pip install -r requirements.txt
```

### 4. Executar as Migrações

Aplique as migrações para criar as tabelas no banco de dados:

```bash

python manage.py migrate
```

### 5. Iniciar o Servidor de Desenvolvimento

Com tudo configurado, execute o servidor localmente:

```bash

python manage.py runserver
```


A aplicação estará disponível em http://127.0.0.1:8000/.


### Endpoints

Aqui estão os principais endpoints da API:

- **GET /api/urls/**: Lista todas as URLs do YouTube.
- **POST /api/urls/**: Adiciona uma nova URL do YouTube.
- **GET /api/urls/`<id>`/**: Recupera uma URL específica pelo seu ID.
- **DELETE /api/urls/`<id>`/**: Deleta uma URL pelo seu ID.

### Melhorias Futuras

- Implementar autenticação para usuários.
- Adicionar paginação à listagem de URLs.
- Adicionar validação mais rigorosa para URLs.
- Melhorar o sistema de logs e monitoramento de erros.

### Observações/Bugs

- URLs inválidas podem ser inseridas sem validação (melhoria futura).
- No momento, não há uma interface para feedback em caso de falhas de requisições.

### Deploy

Para realizar o deploy da aplicação, siga os seguintes passos:

- Configurar as variáveis de ambiente (como SECRET_KEY e detalhes do banco de dados) em seu ambiente de produção.
- Realizar as migrações do banco de dados com python manage.py migrate.
- Usar um servidor de produção adequado (como Gunicorn ou uWSGI) para servir o Django.
- Configurar um servidor web (como Nginx ou Apache) para servir os arquivos estáticos e fazer o proxy reverso para o Django.

### Contribuições

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
