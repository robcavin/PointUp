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