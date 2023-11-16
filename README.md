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
