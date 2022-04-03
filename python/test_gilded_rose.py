# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item_factory import ItemFactory
from item_quality import ItemQuality
from item_sell_in import ItemSellIn


class GildedRoseTest(unittest.TestCase):

    def test_conjured(self):
        items = [ItemFactory.based_on("Conjured Mana Cake", 2, 7)]
        gilded_rose = GildedRose()
        gilded_rose.update_quality(items)
        # print(items[0].quality())
        self.assertEqual(ItemQuality(5), items[0].quality())
        self.assertEqual(ItemSellIn(1), items[0].sell_in())
        # one more day
        gilded_rose.update_quality(items)
        # self.assertEqual(3, gilded_rose.items[0].quality())
        # self.assertEqual(0, gilded_rose.items[0].sell_in())
        # one more day again
        gilded_rose.update_quality(items)
        # self.assertEqual(0, gilded_rose.items[0].quality)
        # self.assertEqual(-1, gilded_rose.items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
