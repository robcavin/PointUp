"""
Django settings for points project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FACEBOOK_APP_ID = '630834406963966'
FACEBOOK_APP_SECRET = '169e943f0c5b9f670c6a92cd013152f8'
FACEBOOK_DEFAULT_SCOPE = ['basic_info', 'email']
FACEBOOK_STORE_LIKES = True
FACEBOOK_STORE_FRIENDS = True
FACEBOOK_CELERY_STORE = True
FACEBOOK_CELERY_TOKEN_EXTEND = True
#FACEBOOK_REGISTRATION_BACKEND = 'django_facebook.registration_backends.FacebookRegistrationBackend'

FACEBOOK_CANVAS_PAGE = 'https://apps.facebook.com/goodpointstest'

# Celery stuff
BROKER_URL = 'redis://app22463601:jyS5FKra9PWXrYRh@pub-redis-16738.us-east-1-3.2.ec2.garantiadata.com:16738/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600,
                            'max_connections': 5}  # 1 hour.  # TODO - Remove Redis connection limit

RAVEN_CONFIG = {
    'dsn': 'https://237a31ed8b584f3abe8bab642f753e55:08f3ee7540c948819e8aa52344eb58b1@app.getsentry.com/19927',
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q7@jh=--=e#713^mns_q#n@#x2%155eu059)43szphhlaex%2#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_facebook',
    'rest_framework',
    'raven.contrib.django.raven_compat',
    'points',
)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'PAGINATE_BY': 10
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_facebook.middleware.FacebookCanvasMiddleWare'
)

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'points.CustomUser'

TEMPLATE_DIRS = (
    'templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                               'django_facebook.context_processors.facebook',
                               'django.core.context_processors.request',
)

ROOT_URLCONF = 'points.urls'

WSGI_APPLICATION = 'points.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'
# Static asset configuration
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

if os.path.isfile(os.path.join(BASE_DIR, 'LOCAL')):
    from settings_local import *