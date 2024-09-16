from pathlib import Path
from dotenv import dotenv_values
from quickreads.utils.constants import (
    LANGUAGE_CODE,
    TIME_ZONE,
    STATIC_URL,
    STATIC_PATH,
    STATIC_ROOT,
    TEMPLATES,
)
import os

config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config.get("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "accounts.apps.AccountsConfig",
    "pyrebase",
    "django_htmx",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "quickreads.utils.login_middleware.LoginMiddleware",
]

ROOT_URLCONF = "quickreads.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, TEMPLATES)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "quickreads.utils.context_processors.theme_form",
                "quickreads.utils.context_processors.newsletter_form",
            ],
        },
    },
]

WSGI_APPLICATION = "quickreads.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = LANGUAGE_CODE

TIME_ZONE = TIME_ZONE

USE_I18N = True

USE_TZ = True

STATIC_URL = STATIC_URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_PATH)]
STATIC_ROOT = STATIC_ROOT

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email Configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_SSL = True  # use port 465
EMAIL_USE_TLS = False  # use port 587
EMAIL_PORT = 465  # OR 587
EMAIL_HOST_USER = config.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config.get("EMAIL_HOST_PASSWORD")
