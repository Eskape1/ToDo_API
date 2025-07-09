from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def hash_psw(password: str) -> str:
    return pwd_context.hash(password)

def verify_psw(secret: str, hash: str) -> bool:
    return pwd_context.verify(secret, hash)