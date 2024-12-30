from model.user import User

fakes =[
    User(
        name="Ulyana",
        hash= "password"
    ),
    User(
        name="b",
        hash= "B"
    ),
]

def find(name: str) -> User | None:
    for e in fakes:
        if e.name == name:
             return e
    return None

def check_missing(name: str):
    if not find(name):
        raise ValueError(f"Missing user {name}")


def check_duplicate(name: str):
    if find(name):
        raise ValueError(f"Missing user {name}")


def get_all() -> list[User]:
     """Возврат всех пользователей"""
     return fakes

def get_one(name: str) -> User:
     """Возврат одного пользователя"""
     return find(name)

def create(user: User) -> User:
    check_duplicate(user.name)
    return user

def modify(name: str, user: User) -> User:
    check_missing(name)
    for i, existing_user in enumerate(fakes):
        if existing_user.name == name:
            fakes[i] = user
            return user


def delete(name: str) -> None:
    check_missing(name)
    return None
