"""
Django settings for blango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from configurations import Configuration, values
import dj_database_url
import os


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = values.ListValue(['*'])
    
    INTERNAL_IPS = values.ListValue(['127.0.0.1'])
    
    
    CSRF_COOKIE_SAMESITE = None
    CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME','localhost') + '-8000.codio.io',
                            "https://*.ngrok.io",
                            ]
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'crispy_forms', 
        'crispy_bootstrap5',
        'blango_auth',
        'blog',
        'debug_toolbar',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'blango.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
            # 'libraries': {
            #     'filter_tags': 'blog.templatetags.blog_extras',
            #     },
        },
    ]

    WSGI_APPLICATION = 'blango.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'CONN_MAX_AGE' : None,
            'OPTIONS': {
                'read_default_file': str(BASE_DIR / 'my.cnf'),
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'TEST': {
                'NAME': 'meta4BED4littlelemonTest'
            }
        },
        'django_default': dj_database_url.config(default=f"sqlite:///{str(BASE_DIR / 'db.sqlite3')}"),
    }


    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

    # The algorithm that Django recommends is actually Argon2,
    # which was the winner of the 2015 Password Hashing Competition.
    # However it is not enabled by default as it requires installing a third party library.

    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('Asia/Tbilisi')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
                },
            },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler", 
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
                },
            },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
            },
        }    
    
    AUTH_USER_MODEL = "blango_auth.User"
    
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'     
    
    ACCOUNT_ACTIVATION_DAYS = 7   
    
    REGISTRATION_OPEN = values.BooleanValue(False)
    
    # social auth
    SITE_ID = 1

    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


class Prod(Dev):

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    
    # SECURITY WARNING: keep the secret key used in production secret!    
    SECRET_KEY = values.SecretValue()

    ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])
    
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler", 
                "stream": "ext://sys.stdout"
                },
            },
        "root": {
            "handlers": ["console"],
            "level": "ERROR",
            }
        }
    