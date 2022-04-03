from item_name import ItemName
from item_sell_in import ItemSellIn
from item_quality import ItemQuality
from standard_item import StandarItem
from aged_brie import AgedBrie
from backstage_passes import BackstagePasses
from sulfuras import Sulfuras
from conjured import Conjured


class ItemFactory:

    @staticmethod
    def based_on(raw_name: str, raw_sell_in: int, raw_quality: int):
        name = ItemName(raw_name)
        sell_in = ItemSellIn(raw_sell_in)
        quality = ItemQuality(raw_quality)

        if name.is_aged_brie(): return AgedBrie(name, sell_in, quality)
        if name.is_backstage_passes(): return BackstagePasses(name, sell_in, quality)
        if name.is_sulfras(): return Sulfuras(name, sell_in, quality)
        if name.is_conjured(): return Conjured(name, sell_in, quality)
        return StandarItem(name, sell_in, quality)
