Formulários
------------

Instalar dependencias de desenvolvimento python:

```
apt-get install build-essential python3-dev
```

Recomendamos o uso de um ambiente virtual (https://docs.python.org/3/library/venv.html)

```
python3 -m venv venv
```

Ativar o ambiente virtual

```
source venv/bin/activate
```

Instalar cross-env

```
sudo npm install --global cross-env
```

Usar versão 18 do node

```
nvm use 18
```

Com seu ambiente virual ativado instale as dependencias do projeto

```
pip install -r requirements.txt
```

Para executar o projeto localmente é necessário utilizar 2 terminais

Terminal1: Servidor do Django resposável por renderizar as páginas

```
python manage.py runserver
```

Terminal2: Script Node JS responsável por compilar o TailwindCSS

```
python manage.py tailwind install
```

```
python manage.py tailwind start
```

Acessar o projeto através da url http://127.0.0.1:8000/
