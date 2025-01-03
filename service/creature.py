import os
from model.creature import Creature
import fake.creature as data

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as data
else:
    from data import creature as data

def get_all() -> list[Creature]:
    return data.get_all()

def get_one(name: str) -> Creature | None:
    return data.get_one(name)

def create(creature: Creature) -> Creature:
    return data.create(creature)

def replace(creature: Creature) -> Creature:
    return data.replace(creature)

def modify(creature: Creature) -> Creature:
    return data.modify(creature)

def delete(name: str) -> bool:
    return data.delete(name)