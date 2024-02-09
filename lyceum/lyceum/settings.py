from os import environ
from pathlib import Path

from dotenv import load_dotenv
from utilities.config import get_env_var


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / "../.env")

SECRET_KEY = get_env_var("DJANGO_SECRET_KEY")

debug_string = get_env_var("DJANGO_DEBUG")
DEBUG = True if debug_string.lower() not in ("", "false") else False

hosts_string = environ.get("DJANGO_ALLOWED_HOSTS")
ALLOWED_HOSTS = hosts_string.split(",") if hosts_string != "" else []


INSTALLED_APPS = [
    "homepage.apps.HomepageConfig",
    "catalog.apps.CatalogConfig",
    "about.apps.AboutConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lyceum.urls"

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

WSGI_APPLICATION = "lyceum.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth."
            "password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth."
            "auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth."
            "password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth."
            "password_validation.NumericPasswordValidator"
        ),
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
