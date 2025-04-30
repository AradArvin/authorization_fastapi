import os.path
from decouple import config


def read_secret_keys(path):
    if os.path.exists(path):
        with open(fr'{path}') as pem_file:
            return pem_file.read()
    else:
        return None


PRIVATE_SECRET_KEY_FILE_PATH = config('PRIVATE_PEM')
PRIVATE_SECRET_KEY = read_secret_keys(PRIVATE_SECRET_KEY_FILE_PATH)
PUBLIC_SECRET_KEY_FILE_PATH = config('PUBLIC_PEM')
PUBLIC_SECRET_KEY = read_secret_keys(PUBLIC_SECRET_KEY_FILE_PATH)
ALGORITHM = config('')


ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7