## Formulários

Instalar dependencias de desenvolvimento python:

```
apt-get install build-essential python3-dev libpq-dev
```

Recomendamos o uso de um ambiente virtual (https://docs.python.org/3/library/venv.html)

```
python3 -m virtualenv venv
```

Ativar o ambiente virtual

```
source venv/bin/activate
```

Instalar cross-env

```
npm install --global cross-env
```

Com seu ambiente virtual ativado instale as dependencias do projeto

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Para executar o projeto localmente é necessário utilizar 2 terminais

Terminal1: Servidor do Django resposável por renderizar as páginas

```
python manage.py runserver
```

Terminal2: Script Node JS responsável por compilar o TailwindCSS

Usar versão 18 do node

```
nvm use 18
```

```
cd theme/
npm i

```

```
npm run dev
```

Acessar o projeto através da url http://127.0.0.1:8000/

## Capacitação Moodle

Utilizamos a plataforma Moodle para realizar a capacitação das voluntárias (psicólogas e advogadas). As orientações sobre modificações na plataforma estão [nessa documentação](https://github.com/mapadoacolhimento/cadastro/tree/feature/moodle-training/moodle-training).

## Static Analysis

### Format

Rodando formatter manualmente em todos os arquivos `.py`.

```bash
black . --extend-exclude="/(theme|cypress|\.github|moodle-training|deploy|migrations)/"
```

### Lint

Rodando lint manualmente em todos os arquivos `.py`.

```bash
pylint --load-plugins pylint_django --django-settings-module=project.settings --rcfile=.pylintrc  $(git ls-files '*.py')
```

## Migrations

### Definindo o banco de dados

Para realizar testes locais antes de publicar suas alteracões nos banco de STG ou PROD, altere a variavel de ambiente `DATABASE_URL` para a URI do seu banco local.

### Executando as migrations

Quando você faz alguma alteracão ao aquivos `models` do seu app, precisa criar uma migration para registrar aquela alteracão na pasta `migrations`.

```bash
python manage.py makemigrations --name [nome da sua migration]
```

Após rodar esse comando, um arquivo será gerado dentro da pasta `[app name]/migrations`.

Para aplicar essas alteracões em seu banco de dados, rode:

```bash
python manage.py migrate
```
