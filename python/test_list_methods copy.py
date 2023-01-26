import unittest
from typing import List

class TestListMethods(unittest.TestCase):
    def test_insert(self) -> None:
        test_list: List[int] = list(range(1, 3)) + list(range(4, 7))
        test_list.insert(2, 3)
        self.assertEqual(test_list, list(range(1, 7)))

    def test_extend(self) -> None:
        test_list: List[int] = list(range(1, 4))
        test_list.extend(range(4, 10))
        self.assertEqual(test_list, list(range(1, 10)))

    def test_find(self) -> None:
        s: str = 'hello world'
        pos: int = s.find('o')
        self.assertEqual(pos, 4)
        pos = s.find('o', 5)
        self.assertEqual(pos, 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)