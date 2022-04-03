# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import GildedRose
from item import Item
from item_factory import ItemFactory

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             ItemFactory.based_on("+5 Dexterity Vest", 10, 20),
             ItemFactory.based_on("Aged Brie", 2, 0),
             ItemFactory.based_on("Elixir of the Mongoose", 5, 7),
             ItemFactory.based_on("Sulfuras, Hand of Ragnaros", 0, 80),
             ItemFactory.based_on("Sulfuras, Hand of Ragnaros", -1, 80),
             ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 15, 20),
             ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 10, 49),
             ItemFactory.based_on("Backstage passes to a TAFKAL80ETC concert", 5, 49),
             ItemFactory.based_on("Conjured Mana Cake", 3, 6),
             ItemFactory.based_on("Conjured Mana Cake", 2, 7),  # <-- :O
            ]

    days = 3
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose().update_quality(items)
