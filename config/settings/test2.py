"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

import os
# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=False)
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='0wG2N60LqkDwM0Vi42p63bTekW3ac7Jt9w140F6YuUzsPcJMynEmFcx5YKlTzlop')
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
	"127.0.0.1",
]
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # Mimicing memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
# TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405
# TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa F405
#     (
#         'django.template.loaders.cached.Loader',
#         [
#             'django.template.loaders.filesystem.Loader',
#             'django.template.loaders.app_directories.Loader',
#         ],
#     ),
# ]

TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]

# Gunicorn
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['gunicorn']  # noqa F405
INSTALLED_APPS += ['bootcamp.qiniustorage']  # noqa F405
# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'localhost'
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# STATIC
# ------------------------
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#enable-whitenoise
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE  # noqa F405

# Your stuff...
# # ------------------------------------------------------------------------------
# STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = '/static/'

QINIU_ACCESS_KEY = '5G9JKa5er7h_Isl3uYus_qBLdgbCbbF-DJ6MLb-n'
QINIU_SECRET_KEY = 'Xz3qJv2IVPYupPExlMEdMvdnD_I4j-Y8dvFLIoDh'
QINIU_BUCKET_NAME = 'duanwo'
QINIU_BUCKET_DOMAIN = 'pb4vviir3.bkt.clouddn.com'
QINIU_SECURE_URL = False      #使用http


PREFIX_URL = 'http://'

# MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'
# MEDIA_ROOT = os.path.join(MEDIA_URL, 'media')

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN+'/media/'
# MEDIA_ROOT = MEDIA_URL
# MEDIA_URL = '/media/'
# MEDIA_ROOT = str(APPS_DIR.path('media'))

# MEDIA_URL = ''
# MEDIA_ROOT = str(APPS_DIR.path('media'))
MEDIA_ROOT = str(APPS_DIR.path('media'))
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'




# STATIC_URL = QINIU_BUCKET_DOMAIN + '/static/'
# # STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'

# LANGUAGE
# LANGUAGES = (
#     ('en', 'English'),
#     ('pt-br', 'Portuguese'),
#     ('es', 'Spanish'),
#     ('zh-cn', 'Chinese'),
# )
#
# LOCALE_PATHS = (str(APPS_DIR.path('locale')), )
LANGUAGE_CODE = 'zh-cn'


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
# ADMIN_URL = env('DJANGO_ADMIN_URL')
# ADMIN_URL = env('DJANGO_ADMIN_URL')

# 使用如下配置即可控制url的位置，但是无法实现上面的方法，在配置文件读取 配置参数
ADMIN_URL = r'^admin/'

