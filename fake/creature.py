from model.creature import Creature


_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Handsome Himalayan"
    ),
    Creature(
        name="Bigfoot",
        aka="Yeti's Cousin Eddie",
        country="US",
        area="*",
        description="Sasquatch"
    ),
]

def get_all() -> list[Creature]:
    """Возврат всех существ"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Возврат одного существа"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# примеры ниже пока не функциональны
def create(creature: Creature) -> Creature:
    """Добавить существо"""
    return creature

def modify(creature: Creature) -> Creature:
    """Частичное изменение записи существа"""
    return creature

def replace(creature: Creature) -> Creature:
    """Полная замена записи существа"""
    return creature

def delete(name: str) -> bool | None:
    """Удаление записи существа; возврат значения None,
    если запись существовала"""
    return None