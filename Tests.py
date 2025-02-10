import unittest
from suma import suma, resta


class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(4, 5), 9)

    def test_resta(self):
        self.assertEqual(resta(4, 5), -1)


if __name__ == '__main__':
    unittest.main()