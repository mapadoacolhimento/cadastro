# Build staticfiles
FROM node:latest AS node-builder

WORKDIR /app

COPY . .

WORKDIR /app/theme

RUN npm i

RUN npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css

# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:slim-buster

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Django CMS and Django.
# RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
#     build-essential \
#     cargo \
#     libssl-dev \
#     libffi-dev \
#     sox \
#     ffmpeg \
#     libcairo2 \
#     libcairo2-dev \
#     python3-dev \
# && rm -rf /var/lib/apt/lists/*

# # Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install uwsgi
# Install the project requirements.
COPY requirements.txt /
RUN pip install -r requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Copy the source code of the project into the container.
COPY --from=node-builder /app ./

RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called.
CMD ["uwsgi", "--ini", "--vhost", "/app/deploy/wsgi.ini"]