"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import environ
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(
        str,
        "django-insecure-cx!j1+m*n87=*iq%m8!^$d8tf0%%=muz4lb5bf4p7h8=zpgfe)",
    ),
    ALLOWED_HOSTS=(list, ["*"]),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-favulwz7_kl&ri+^#t)p8miu=$tag@=o&b%%s%fr-ghez)2g)z'
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = env("DEBUG")

ALLOWED_HOSTS: "list[str]" = env("ALLOWED_HOSTS")

MSR_HOST = env("MSR_HOST", default="queroseracolhida.dev:8000")

VOLUNTEER_HOST = env("VOLUNTEER_HOST", default="queroacolher.dev:8000")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "theme",
    "msrs.apps.MsrsConfig",
    "volunteers.apps.VolunteersConfig",
    "volunteers.bonde",
    "volunteers.moodle",
]

MIDDLEWARE = [
    "project.virtualhostmiddleware.VirtualHostMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# from django.forms.renderers import TemplatesSetting


# class DaisyUIFormRenderer(TemplatesSetting):
#     form_template_name = 'daisyui/form.html'


# FORM_RENDERER = "project.settings.DaisyUIFormRenderer"

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEFAULT_DB_SQLITE = BASE_DIR / "db.sqlite3"
BONDE_DB_SQLITE = BASE_DIR / "bonde.sqlite3"
MOODLE_DB_SQLITE = BASE_DIR / "moodle.sqlite3"

DATABASES = {
    "default": env.db_url("DATABASE_URL", f"sqlite:///{DEFAULT_DB_SQLITE}"),
    "bonde": env.db_url("BONDE_DATABASE_URL", f"sqlite:///{BONDE_DB_SQLITE}"),
    "moodle": env.db_url("MOODLE_DATABASE_URL", f"sqlite:///{MOODLE_DB_SQLITE}"),
}

DATABASE_ROUTERS = [
    "volunteers.bonde.router.AuthRouter",
    "volunteers.moodle.router.AuthRouter",
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles_collected"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MOODLE_API_URL = env("MOODLE_API_URL", default="https://moodle.site.com")

MOODLE_API_KEY = env("MOODLE_API_KEY", default="XXXXXXXXX")

MOODLE_DEFAULT_PASS = env("MOODLE_DEFAULT_PASS", default="XXXXXXXXX")

GEOCODING_API_KEY = env("GEOCODING_API_KEY", default="XXXXXXXXX")

GOOGLE_MAPS_API_KEY = env("GOOGLE_MAPS_API_KEY", default="XXXXXXXXX")

LOOPS_API_KEY = env("LOOPS_API_KEY", default="XXXXXXXXXXXX")

ZENDESK_SUBDOMAIN = env("ZENDESK_SUBDOMAIN", default="https://example.zendesk.com")
ZENDESK_API_TOKEN = env("ZENDESK_API_TOKEN", default="XXXXXXXXXXXX")
ZENDESK_API_USER = env("ZENDESK_API_USER", default="XXXXXXXXXXXX")

META_PIXEL_ID = env('META_PIXEL_ID', default=None)