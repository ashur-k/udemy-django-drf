from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure--!y5y+vof*1rf4!z$=(h16&ra8x7r%mdydy!x^=f(mxz@osmvi'
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]