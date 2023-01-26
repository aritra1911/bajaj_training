import unittest
from calc import Calculator

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Calculator(9, 6)
        self.f = open('test_results.log', 'w')
        return super().setUp()

    def test_sum(self) -> None:
        self.assertEqual(self.c.get_addition(), 15, 'The sum is wrong')

    def test_difference(self) -> None:
        self.assertEqual(self.c.get_difference(), 3, 'The difference is wrong')

    def test_product(self) -> None:
        self.assertEqual(self.c.get_product(), 54, 'The difference is wrong')

    def test_division(self) -> None:
        self.assertEqual(self.c.get_division(), 1, 'The difference is wrong')

    def tearDown(self) -> None:
        self.f.close()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()