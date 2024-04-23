import unittest

def greater_number(x, y, z):
    # Comparer les trois nombres pour trouver le plus grand
    greater_number = x
    if y > greater_number:
        greater_number = y
    if z > greater_number:
        greater_number = z
    return greater_number

class TestGreaterNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(greater_number(1, 2, 3), 3)

    def test_negative_numbers(self):
        self.assertEqual(greater_number(-1, -2, -3), -1)

    def test_mixed_numbers(self):
        self.assertEqual(greater_number(-1, 2, 0), 2)

    def test_equal_numbers(self):
        self.assertEqual(greater_number(3, 3, 3), 3)

if __name__ == '__main__':
    unittest.main()
