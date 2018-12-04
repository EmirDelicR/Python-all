import unittest
import circles
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEquals(circles.circle_area(1), pi)


# call in terminal python -m unittest circles_test
