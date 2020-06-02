from portfolio.settings.base import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'],
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT']
    }
}
