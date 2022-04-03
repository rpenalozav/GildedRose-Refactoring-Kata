from __future__ import annotations


class ItemQuality:
    MAX_VALUE: int = 50
    MIN_VALUE: int = 0

    def __init__(self, value):
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

    def __hash__(self):
        return hash(self._value)
