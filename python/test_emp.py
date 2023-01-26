import unittest
from emp import Emp

class TestEmp(unittest.TestCase):
    def setUp(self) -> None:
        self.emp = Emp('E001', 'Kapil', 50000.00)
        return super().setUp()

    def test_id(self) -> None:
        self.assertEqual(self.emp.get_id(), 'E001')

    def test_name(self) -> None:
        self.assertEqual(self.emp.get_name(), 'Kapil')

    def test_difference(self) -> None:
        self.assertEqual(self.c.get_difference(), 3, 'The difference is wrong')

    def test_product(self) -> None:
        self.assertEqual(self.c.get_product(), 54, 'The difference is wrong')

    def test_division(self) -> None:
        self.assertEqual(self.c.get_division(), 1, 'The difference is wrong')

    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()