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
        self.assertEqual(hash(ItemQuality(5)), hash(items[0].quality()))
        self.assertEqual(hash(ItemSellIn(1)), hash(items[0].sell_in()))
        # one more day
        gilded_rose.update_quality(items)
        self.assertEqual(hash(ItemQuality(3)), hash(items[0].quality()))
        self.assertEqual(hash(ItemSellIn(0)), hash(items[0].sell_in()))
        # one more day again
        gilded_rose.update_quality(items)

if __name__ == '__main__':
    unittest.main()
