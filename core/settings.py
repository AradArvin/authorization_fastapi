import os.path
from decouple import config
from cryptography.hazmat.primitives import serialization


PEM_PASS_STR = config('PEM_PASS')
PEM_PASS = bytes(PEM_PASS_STR, 'utf-8')

def read_secret_keys(path, is_private=False):
    if os.path.exists(path):
        if is_private:
            with open(fr'{path}', 'rb') as key_file:
                return serialization.load_pem_private_key(key_file.read(), password=PEM_PASS)
        else:
            with open(fr'{path}', 'rb') as key_file:
                return  serialization.load_pem_public_key(key_file.read())
    else:
        return None


PRIVATE_SECRET_KEY_FILE_PATH = config('PRIVATE_PEM')
PRIVATE_SECRET_KEY = read_secret_keys(PRIVATE_SECRET_KEY_FILE_PATH, is_private=True)

PUBLIC_SECRET_KEY_FILE_PATH = config('PUBLIC_PEM')
PUBLIC_SECRET_KEY = read_secret_keys(PUBLIC_SECRET_KEY_FILE_PATH)

ALGORITHM = config('ALGORITHM')


ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7


REDIS_HOST_ADDRESS = "redis://127.0.0.1:6379/0"