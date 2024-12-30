import os
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User
# if os.getenv("CRYPTID_UNIT_TEST"):
#     from fake import user as service
# else:
#     from service import user as service

from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

# Эта зависимость создает сообщение в каталоге
# "/user/token" (из формы с именем пользователя и паролем)
# и возвращает токен доступа.
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")

def unauthed():
     raise HTTPException(
         status_code=401,
         detail="Incorrect username or password",
         headers={"WWW-Authenticate": "Bearer"},
        )

# К этой конечной точке направляется любой вызов,
# содержащий зависимость oauth2_dep():
@router.post("/token")
async def create_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
     """Получение имени пользователя и пароля
     из формы OAuth, возврат токена доступа"""
     user = service.auth_user(form_data.username, form_data.password)
     print(user.username, user.password)
     if not user:
        unauthed()

     expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     access_token = service.create_access_token(
        data2={"sub": user.username}, expires=expires
     )
     return {"access_token": access_token, "token_type": "bearer"}

@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
     """Возврат текущего токена доступа"""
     return {"token": token}

# --- предыдущий материал CRUD
@router.get("/")
def get_all() -> list[User]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> User:
    try:
        return service.get_one(name)
    except Exception:
        raise HTTPException(status_code=404)


@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Exception:
        raise HTTPException(status_code=409)

@router.patch("/")
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Exception:
        raise HTTPException(status_code=404)

@router.delete("/{name}")
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Exception:
        raise HTTPException(status_code=404)


