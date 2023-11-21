from .base import *
import dj_database_url
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
       #local
        #'NAME': 'videoteca2',
        #'USER':'root',
        #'PASSWORD':'',
        #'HOST':'localhost',
        #'PORT':'3306',
        #production
        'NAME': 'sccotvideo',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
DATABASES["default"] = dj_database_url.parse("postgres://djangovideoteca_user:26KLVuDsZL6Uejq906g2np7FbTPAsA6r@dpg-cldv4g6f27hc738oqrag-a.oregon-postgres.render.com/djangovideoteca")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'