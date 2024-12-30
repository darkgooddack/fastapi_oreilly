from datetime import timedelta, datetime
from fastapi import HTTPException
from jose import jwt, JWTError
from model.user import User
from passlib.context import CryptContext


# if os.getenv("CRYPTID_UNIT_TEST"):
#     from fake import user as data
# else:
#     from data import user as data

from fake import user as data

SECRET_KEY = "keep"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain: str, hash2: str) -> bool:
    return pwd_context.verify(plain, hash2)

def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)

def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except JWTError:
        return None
    return username

def get_current_user(token: str) -> User | None:
    if not (username := get_jwt_username(token)):
        return None
    if (User := lookup_user(username)):
        return User
    return None


def lookup_user(username: str) -> User | None:
    if (User := data.get_one(username)):
        return User
    return None


def auth_user(name: str, plain: str) -> User | None:
    user = lookup_user(name)
    if not user or not verify_password(plain, user.hash):
        return None
    return user

def create_access_token(data2: dict, expires: timedelta | None = None):
    src = data2.copy()
    now = datetime.now()
    if expires is None:
        expires = timedelta(minutes=15)  # Set a default expiration of 15 minutes
    src.update({"exp": now + expires})
    encoded_jwt = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# --- CRUD-пассивный материал

def get_all() -> list[User]:
    return data.get_all()

def get_one(name) -> User:
    return data.get_one(name)

def create(user: User) -> User:
    return data.create(user)

def modify(name: str, user: User) -> User:
    return data.modify(name, user)

def delete(name: str) -> None:
    return data.delete(name)

