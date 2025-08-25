import unittest
from calculator import operations

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operations.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(operations.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
