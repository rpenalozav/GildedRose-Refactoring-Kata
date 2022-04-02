from __future__ import annotations


class ItemSellIn:

    def __init__(self, value: int):
        self._value = value

    def decrease(self) -> ItemSellIn:
        return ItemSellIn(self._value - 1)

    def is_less_than(self, days: int) -> bool:
        return self._value < days

    def equals(self, o: object) -> bool:
        if self == o:
            return True
        if not isinstance(o, ItemSellIn):
            return False
        that: ItemSellIn = o
        return object.__eq__(self._value, that._value)

    def hash_code(self):
        return object.__hash__(self._value)

