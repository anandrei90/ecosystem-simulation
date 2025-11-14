import unittest
from ecosystem.utils.helpers import distance


class TestDistance(unittest.TestCase):
    """Unit tests for the distance() function."""

    def test_zero_distance(self):
        """Distance between identical points should be zero."""
        self.assertEqual(distance((0, 0), (0, 0)), 0.0)

    def test_horizontal_distance(self):
        """Distance on a horizontal line should be abs(x1 - x2)."""
        self.assertEqual(distance((2, 5), (7, 5)), 5.0)

    def test_vertical_distance(self):
        """Distance on a vertical line should be abs(y1 - y2)."""
        self.assertEqual(distance((3, 4), (3, 10)), 6.0)

    def test_general_distance(self):
        """General case: check against known exact values."""
        self.assertAlmostEqual(distance((0, 0), (3, 4)), 5.0)
        self.assertAlmostEqual(distance((1, 2), (4, 6)), 5.0)


if __name__ == "__main__":
    unittest.main()
