from pathlib import Path
import sys, os
from dotenv import dotenv_values

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(os.path.join(BASE_DIR, 'apps'))

ENV = dotenv_values(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = ENV.get('SECRET_KEY')

DEBUG = True

AUTH_USER_MODEL = 'accounts.User'

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'contents',
    'main',
    'auction'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.routing.application'

SITE_URL = 'http://192.168.1.157:8000/en/'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sanart',
        'USER': 'sanart',
        'PASSWORD': 'sanart',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English')
)

DEFAULT_LANGUAGE = 1

LANGUAGE_CODE = 'uz'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')

MODELTRANSLATION_TRANSLATION_FILES = (
    'main.translation',
)

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    },
    'DOC_EXPANSION': 'none',
}
