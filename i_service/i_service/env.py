from envparse import Env

env = Env(
    DATABASE_USER=dict(cast=str),
    DATABASE_PASSWORD=dict(cast=str),
    DATABASE_NAME=dict(cast=str),
    ALLOWED_HOSTS=dict(cast=list),
    SECRET_KEY=dict(cast=str),
    PROXY_IMAGES_DIR=dict(cast=str),
    PROXY_IMAGES_URL=dict(cast=str),
    PROXY_FOR_INSTAGRAM=dict(cast=str)
)

env.read_envfile()
