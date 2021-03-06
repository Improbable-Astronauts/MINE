"""
Django settings for movie_review project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
import omdb
from .hidden import (SECRET_KEY, omdb_key, Gmail_PASS, DB_USER, DB_PASS, SENDGRID_PASS,
                    SENDGRID_USERNAME)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['improb-astro.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'movie_review.urls'

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

WSGI_APPLICATION = 'movie_review.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    #local postgres db
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'basicmovies',
    #     'USER': 'timmy',
    #     'PASSWORD': 'home99run',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
    # Below works with whitenoise
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        }
    #''' running heroku db setting '''
    #  'default': {
        

    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'dk8043rlo251b',
    #         'USER': DB_USER,
    #         'PASSWORD': DB_PASS,
    #         'HOST': 'ec2-23-23-130-158.compute-1.amazonaws.com',
    #         'PORT': '5432',
    #     }

}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),

)
# for gzip functionality
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# OMDB settings
API_KEY = omdb_key
omdb.set_default('apikey', API_KEY)

#set up smtp for sharing reviews local only
'''
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jasonr.jones14@gmail.com' # if using gmail don't forget to turn on access for less secure apps
EMAIL_HOST_PASSWORD = Gmail_PASS
EMAIL_PORT = 587
EMAIL_USE_TLS = True
'''

# using sendgrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = SENDGRID_USERNAME
EMAIL_HOST_PASSWORD = SENDGRID_PASS
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = ''

# Configure Django App for Heroku.
django_heroku.settings(locals())


