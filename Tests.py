import unittest
from suma import suma


class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(4, 5), 9)


if __name__ == '__main__':
    unittest.main()