from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from model.user import User, SUser
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, delete


async def get_one(name: str, db: AsyncSession) -> User:
    query = select(User).where(SUser.name == name)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise ValueError(f"User {name} not found")
    return User.model_validate(user)


async def get_all(db: AsyncSession) -> List[User]:
    query = select(User)
    result = await db.execute(query)
    users = result.scalars().all()
    return [User.model_validate(user) for user in users]


async def create(user: User, db: AsyncSession) -> User:
    new_user = User(name=user.name, hash=user.hash)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)  # Обновляем объект из БД
        return User.model_validate(new_user)
    except IntegrityError:
        await db.rollback()
        raise ValueError(f"User {user.name} already exists")


async def modify(name: str, updated_data: User, db: AsyncSession) -> User:
    query = (
        update(User)
        .where(SUser.name == name)  # Условие
        .values(name=updated_data.name, hash=updated_data.hash)
        .returning(User)  # Возвращаем обновлённого пользователя
    )
    result = await db.execute(query)
    updated_user = result.scalar_one_or_none()
    if updated_user is None:
        raise ValueError(f"User {name} not found")
    await db.commit()
    return User.model_validate(updated_user)


async def delete_user(name: str, db: AsyncSession) -> None:
    query = delete(User).where(SUser.name == name)
    result = await db.execute(query)
    if result.rowcount == 0:
        raise ValueError(f"User {name} not found")
    await db.commit()