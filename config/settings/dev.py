from .base import *  # noqa

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, "moat-server/env.dev"))

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}
