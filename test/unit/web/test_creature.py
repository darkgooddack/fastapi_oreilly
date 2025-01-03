from fastapi import HTTPException
import pytest
import os
os.environ["CRYPTIC_UNIT_TEST"] = "true"
from model.creature import Creature
from web import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="dragon",
        description="Wings! Fire! Aieee!",
        country="*"
    )

@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()

def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]

def test_modify(fakes):
    assert creature.modify(fakes[0]) == fakes[0]

def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None