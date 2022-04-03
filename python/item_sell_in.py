from __future__ import annotations


class ItemSellIn:

    def __init__(self, value: int):
        self._value = value

    def decrease(self) -> ItemSellIn:
        return ItemSellIn(self._value - 1)

    def is_less_than(self, days: int) -> bool:
        return self._value < days

    # def __repr__(self):
    #     return "%s" % self._value
