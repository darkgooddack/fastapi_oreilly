import os
from model.creature import Creature
import pytest

os.environ["CRYPTIC_UNIT_TEST"] = "true"
from fake import creature as data

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Handsome Himalayan"
    )

def test_create(sample):
    resp = data.create(sample)
    assert resp == sample

def test_get_exists(sample):
    resp = data.create(sample)
    assert resp == sample
    resp = data.get_one(sample.name)
    assert resp == sample

def test_modify(sample):
    sample.country = "CA"
    resp = data.modify(sample)
    assert resp == sample

