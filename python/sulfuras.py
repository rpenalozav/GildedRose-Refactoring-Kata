from item import Item
from item_name import ItemName
from item_sell_in import ItemSellIn
from item_quality import ItemQuality


class Sulfuras(Item):
    DOUBLE_QUALITY_DECREASE_SELL_IN_THRESHOLD: int = 0

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super().__init__(name, sell_in, quality)

    def update(self):
        pass