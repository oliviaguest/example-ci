import unittest

from my_func import my_func


class TestMy_Sum(unittest.TestCase):
    """Test pdist."""

    def test_my_func(self):
        self.assertTrue(my_func(3, 5) == 8)
        self.assertTrue(my_func(1000, 2000) == 3000)
        self.assertTrue(my_func(1, 1) == 0)


if __name__ == '__main__':
    unittest.main()
