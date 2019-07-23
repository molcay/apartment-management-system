from project.settings.base import *

ALLOWED_HOSTS += [
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='sxakk)#c&kz$%jn6i_1*7i!5_j2f1k*$l-hnc&@dzverz4$ooz')
DEBUG = env.bool('DJANGO_DEBUG', True)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INSTALLED_APPS += [
]
