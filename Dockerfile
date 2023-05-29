FROM python:3.9

RUN apt install curl

RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -

RUN apt update -y

RUN apt upgrade -y

RUN apt install -y nodejs

WORKDIR /app

COPY ./ /app

WORKDIR /app/theme

RUN npm i

RUN npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css

WORKDIR /app

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD uwsgi --http=0.0.0.0:80 --module=project.wsgi --honour-stdin