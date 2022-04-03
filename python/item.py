from abc import ABC, abstractmethod
from item_quality import ItemQuality
from item_sell_in import ItemSellIn
from item_name import ItemName


class Item(ABC):

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        self._name = name
        self._sell_in = sell_in
        self._quality = quality

    @abstractmethod
    def update(self):
        pass

    def sell_in(self) -> ItemSellIn:
        return self._sell_in

    def quality(self) -> ItemQuality:
        return self._quality

    def decrease_sell_in(self) -> None:
        self._sell_in = self._sell_in.decrease()

    def has_to_be_sold_in_less_than(self, days: int) -> bool:
        return self._sell_in.is_less_than(days)

    def increase_quality(self) -> None:
        self._quality = self._quality.increase()

    def decrease_quality(self) -> None:
        self._quality = self._quality.decrease()

    def reset_quality(self) -> None:
        self._quality = self._quality.reset()

    def __repr__(self):
        return "%s, %s, %s" % (self._name, self._sell_in, self._quality)
