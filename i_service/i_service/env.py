from envparse import Env

env = Env(
    DATABASE_USER=dict(cast=str),
    DATABASE_PASSWORD=dict(cast=str),
    DATABASE_NAME=dict(cast=str),
    ALLOWED_HOSTS=dict(cast=list),
)

env.read_envfile()
