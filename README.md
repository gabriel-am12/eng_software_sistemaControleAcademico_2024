### Programas Necessários
  1. Python 3.x

  2. Django é um framework Python, então você precisa ter o Python instalado no seu sistema.
  [Download Python](https://www.python.org/downloads/)

  3. Virtualenv (opcional, mas recomendado)
  Virtualenv é uma ferramenta para criar ambientes virtuais Python. É útil para isolar as dependências do projeto.  
  Para instalar o Virtualenv:
  `pip install virtualenv`

### Configuração do Ambiente
  1. Criar e ativar um ambiente virtual
     * Crie um novo ambiente virtual (substitua env pelo nome que preferir)  
     `python -m venv env`
     * Ative o ambiente virtual
       * No Windows  
       `.\env\Scripts\activate`
       * No Linux  
       `source env/bin/activate`
  1. Instalar Django  
     `pip install django`

### Rodar o servidor de desenvolvimento  
  1.  `python manage.py runserver`
  2.  Abra o navegador e vá para 'http://127.0.0.1:8000'
