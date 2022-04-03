from item import Item
from item_name import ItemName
from item_sell_in import ItemSellIn
from item_quality import ItemQuality


class AgedBrie(Item):
    DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD: int = 0

    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.decrease_sell_in()
        self.increase_quality()

        if self.has_to_be_sold_in_less_than(AgedBrie.DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD):
            self.increase_quality()
