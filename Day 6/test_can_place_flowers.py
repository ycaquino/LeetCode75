import unittest
import canPlaceFlowers


class TestCanPlaceFlowers(unittest.TestCase):
    def test_can_place_flowers(self):
        self.assertEqual(canPlaceFlowers.can_place_flowers([1, 0, 0, 0, 1], 1), True)
        self.assertEqual(canPlaceFlowers.can_place_flowers([1, 0, 0, 0, 1], 2), False)
        self.assertEqual(canPlaceFlowers.can_place_flowers([0], 1), True)
        self.assertEqual(canPlaceFlowers.can_place_flowers([1, 0], 1), False)
        self.assertEqual(canPlaceFlowers.can_place_flowers([0, 0, 1, 0, 0], 1), True)
