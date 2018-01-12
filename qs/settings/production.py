
from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='postgres://mzobacrcbcbfzz:0355b0d7b00b0f16818714bbc8f3f2f92026e4cd5fbc979eab7ea7da31c1dd30@ec2-54-217-218-80.eu-west-1.compute.amazonaws.com:5432/ddadu6455cjs4u'
)