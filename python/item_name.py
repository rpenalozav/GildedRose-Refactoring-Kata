class ItemName:
    AGED_BRIE: str = "Aged Brie"
    BACKSTAGE_PASSES: str = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS: str = "Sulfuras, Hand of Ragnaros"
    CONJURED: str = "Conjured Mana Cake"

    def __init__(self, value: str):
        self._value: str = value

    def is_aged_brie(self):
        return ItemName.AGED_BRIE.__eq__(self._value)

    def is_backstage_passes(self):
        return ItemName.BACKSTAGE_PASSES.__eq__(self._value)

    def is_sulfras(self):
        return ItemName.SULFURAS.__eq__(self._value)

    def is_conjured(self):
        return ItemName.CONJURED.__eq__(self._value)

    def equals(self, o: object) -> bool:
        if self == o:
            return True
        if not isinstance(o, ItemName):
            return False
        that: ItemName = o
        return object.__eq__(self._value, that._value)

    def hash_code(self):
        return object.__hash__(self._value)
