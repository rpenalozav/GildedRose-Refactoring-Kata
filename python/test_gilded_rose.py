# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item_factory import ItemFactory


class GildedRoseTest(unittest.TestCase):

    def test_conjured(self):
        items = [ItemFactory.based_on("Conjured Mana Cake", 2, 7)]
        gilded_rose = GildedRose()
        gilded_rose.update_quality(items)
        self.assertEqual(5, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        # one more day
        gilded_rose.update_quality()
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        # one more day again
        gilded_rose.update_quality()
        # self.assertEqual(0, gilded_rose.items[0].quality)
        # self.assertEqual(-1, gilded_rose.items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
