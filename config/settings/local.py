import os

from config.settings.base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRESQL_DATABASENAME", "database"),
        "USER": os.getenv("POSTGRESQL_USERNAME", "user"),
        "PASSWORD": os.getenv("POSTGRESQL_PASSWORD", "password"),
        "HOST": os.getenv("POSTGRESQL_HOST", "db"),
        "PORT": os.getenv("POSTGRESQL_PORT", "5432"),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "/static/"
