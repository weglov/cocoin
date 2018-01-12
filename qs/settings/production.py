
from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='postgres://jmhwrltxbineri:d18d3b3e3342410e07312c7f124b7ddc06be69037c71b49e9fc4e584cd445f70@ec2-54-217-218-80.eu-west-1.compute.amazonaws.com:5432/d45t5k25g6o549'
)