from portfolio.settings.base import *


SECRET_KEY = 'mi@*&5a)m-$zd5)dgmyns$4d^4ottac!6+hj3h7)zo50v1dp)2'



DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}
