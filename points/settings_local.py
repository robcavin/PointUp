DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'point',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}

BROKER_URL = 'redis://localhost:6379/0'
CELERY_ALWAYS_EAGER = True

FACEBOOK_APP_ID = '607666135977878'
FACEBOOK_APP_SECRET = '19a0658ce8b736c967cfb6b0ee2b8b13'
