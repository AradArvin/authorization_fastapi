import os
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from core.settings import PEM_PASS


def set_permission_for_files(path, mode):
    os.chmod(path, mode)


def write_secret_keys(path, key):
    with open(fr'{path}.pem', 'wb') as pem_file:
        pem_file.write(key)


def generate_secrets():
    private_key = ec.generate_private_key(ec.SECP256R1(), backend=default_backend())
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(PEM_PASS)
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    write_secret_keys('private', private_pem)
    write_secret_keys('public', public_pem)

    set_permission_for_files('private.pem', 0o600)
    set_permission_for_files('public.pem', 0o644)




