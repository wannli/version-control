from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGE_ME")
ALGORITHM = config("ALGORITHM", cast=str, default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="localhost")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

FIRST_SUPERUSER = config("FIRST_SUPERUSER", cast=str)
FIRST_SUPERUSER_PASSWORD = config("FIRST_SUPERUSER_PASSWORD", cast=Secret)

USERS_OPEN_REGISTRATION = config("USERS_OPEN_REGISTRATION", cast=bool, default=False)