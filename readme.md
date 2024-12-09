# Projeto Django - Gerenciamento de Produtos

Este é um projeto Django simples para gerenciar produtos. Ele permite adicionar, listar, editar e excluir produtos. O projeto inclui formulários personalizados, como a adição de classes CSS dinâmicas nos campos do formulário.

## Pré-requisitos

Antes de rodar o projeto, você precisa ter as seguintes ferramentas instaladas:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Django 3.x ou superior
- Virtualenv (opcional, mas recomendado para criar ambientes isolados)

## Usuário Padrão

O projeto possui um usuário padrão para facilitar o acesso inicial. O usuário foi configurado com o nome `felipe` e a senha `12345`.

### Credenciais para Acesso

- **Usuário**: felipe
- **Senha**: 12345

Essas credenciais podem ser usadas para fazer login no painel administrativo do Django, acessando o seguinte URL:

<http://127.0.0.1:8000/admin/>

Caso deseje criar outros usuários, você pode fazê-lo diretamente pelo painel ou utilizando o comando:

```bash
python manage.py createsuperuser
```

Com isso, você poderá criar um novo superusuário para gerenciar o projeto.

## Configuração do Ambiente

1. **Clone o repositório:**

   Primeiro, faça o clone do repositório para a sua máquina local:

   ```bash
   git clone https://seu-repositorio-url.git
   cd nome-do-repositorio
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   Se você ainda não tem o virtualenv instalado, pode instalá-lo com o seguinte comando:

   ```bash
   pip install virtualenv
   ```

   Para criar e ativar o ambiente virtual:

   - No Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   - No macOS/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   Instale as dependências necessárias do projeto usando o pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do Banco de Dados:**

   O Django usa um banco de dados SQLite por padrão, mas você pode configurá-lo para usar outro banco de dados se necessário.

   Para preparar o banco de dados, execute as migrações:

   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o painel de administração (opcional):**

   Para acessar o painel de administração do Django, crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

   Siga as instruções para criar o superusuário.
   <br>

6. **Inicie o servidor de desenvolvimento:**

   Agora, você pode rodar o servidor de desenvolvimento do Django:

   ```bash
   python manage.py runserver
   ```

### Estrutura de Diretórios

Aqui está uma visão geral da estrutura de diretórios do projeto:

```bash
/projeto_integrador
│
├── manage.py # Script principal para rodar o projeto
├── db.sqlite3 # Banco de dados
├── /projeto_integrador # Diretório do projeto Django (com configurações e URLs)
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py # Configurações do Django
│ ├── urls.py # URLs do projeto
│ └── wsgi.py
│
├── /product # Aplicativo que lida com a funcionalidade dos produtos
│ ├── **init**.py
│ ├── admin.py # Registra modelos no admin
│ ├── apps.py
│ ├── models.py # Modelos de dados
│ ├── tests.py
│ ├── views.py # Lógica das views
|
├── /migrations
│ ├── **init**.py
│ ├── 0001_initial.py
│ └── 0002_alter_produto_nome.py
│
├── /templates # Arquivos de template HTML
│ ├── base.html # Template base
│ ├── product-confirm-delete.html
│ ├── product-details.html
│ ├── product-form.html # Formulário de adição e edição de produtos
│ └── product-list.html
|
├── /templates # Arquivos de template HTML
│ ├── **init**.py
│ └── custom_tags.py
│
└── requirements.txt # Dependências do projeto
```

### Funcionalidades

- Listagem de Produtos: Acesse uma lista de todos os produtos no sistema.
- Adicionar Produto: Formulário para adicionar um novo produto ao sistema.
- Editar Produto: Formulário para editar um produto existente.
- Excluir Produto: Confirmação de exclusão de um produto.
- Administração: Acesse o painel administrativo do Django para gerenciar produtos e outros dados.

### Personalizações

Este projeto inclui uma custom tag para adicionar classes CSS aos campos de formulário. Aqui está um exemplo de como usar a tag add_class para adicionar a classe form-control ao campo de formulário:

```bash
{{ form.nome|add_class:"form-control" }}
```

### Dependências

- Django
- Outras dependências podem ser listadas no requirements.txt

### Licença

Este projeto está licenciado sob a MIT License.
