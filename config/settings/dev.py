from .base import *  # noqa

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, "config/.env.dev"))

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
