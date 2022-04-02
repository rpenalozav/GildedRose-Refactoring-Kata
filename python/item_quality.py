from __future__ import annotations


class ItemQuality:
    MAX_VALUE: int = 50
    MIN_VALUE: int = 0

    def __init__(self, value):
        if value < ItemQuality.MIN_VALUE or value > ItemQuality.MAX_VALUE:
            self._value: int = value

    def increase(self) -> ItemQuality:
        if self._value == ItemQuality.MAX_VALUE:
            return self
        return ItemQuality(self._value + 1)

    def decrease(self) -> ItemQuality:
        if self._value == ItemQuality.MIN_VALUE:
            return self
        return ItemQuality(self._value - 1)

    def reset(self) -> ItemQuality:
        return ItemQuality(ItemQuality.MIN_VALUE)

    def equals(self, o: object) -> bool:
        if self == o:
            return True
        if not isinstance(o, ItemQuality):
            return False
        that: ItemQuality = o
        return object.__eq__(self._value, that._value)

    def hash_code(self):
        return object.__hash__(self._value)
