import unittest
from get_area import *


class TestArea(unittest.TestCase):
    def test_circle(self):
        res = circle(5)
        self.assertEqual(res, 78.53981633974483)
        res = circle(1)
        self.assertEqual(res, math.pi)

    def test_triangle(self):
        res = triangle(5, 4, 6.4031242374328485)
        self.assertEqual(res, 10)
        res = triangle(5, 5, 7.0710678118654755)
        self.assertEqual(res, 12.5)


