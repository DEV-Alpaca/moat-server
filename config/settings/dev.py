from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ
DEBUG = True

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".dev.env"))

# https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Database ------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}
