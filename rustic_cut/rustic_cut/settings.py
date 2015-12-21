"""
Django settings for rustic_cut project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from rustic_cut.common import *


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+1nloazejpnfj6uvwx-@+my6x1in54asyw=1vza^8wzx9=d)yr'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


if not DEBUG:
    # AWS_S3_SECURE_URLS = False

    DEFAULT_FILE_STORAGE = 'rustic-cut.storage.MediaRootS3Storage'
    STATICFILES_STORAGE = 'rustic-cut.storage.StaticRootS3Storage'

    STATIC_URL = '//rustic-cut-dev.s3.amazonaws.com/static/'
    MEDIA_URL = '//rustic-cut-dev.s3.amazonaws.com/media/'
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/static'
    MEDIA_ROOT = '/media'
