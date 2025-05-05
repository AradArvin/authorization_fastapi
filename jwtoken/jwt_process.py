from jose import jwt
from uuid import uuid4
from datetime import datetime, timezone, timedelta
from core.settings import PRIVATE_SECRET_KEY, PUBLIC_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS


def jwt_encoder(payload):
    return jwt.encode(payload, PRIVATE_SECRET_KEY, ALGORITHM)


def jwt_decoder(token):
    return jwt.decode(token, PUBLIC_SECRET_KEY, ALGORITHM)


def generate_jti():
    jti = str(uuid4())
    return jti


async def generate_access_token(jti, user_id):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = dict()
    payload['sub'] = user_id
    payload['jti'] = jti
    payload['exp'] = expire
    payload['iat'] = iat
    payload['type'] = 'access'

    return jwt_encoder(payload)


async def generate_refresh_token(jti, user_id):
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = dict()
    payload['sub'] = user_id
    payload['jti'] = jti
    payload['exp'] = expire
    payload['iat'] = iat
    payload['type'] = 'refresh'

    return jwt_encoder(payload)