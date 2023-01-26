import unittest
from mockito import when, verifyStubbedInvocationsAreUsed
import test_math

class SimpleMockitoTest(unittest.TestCase):
    def test_two_plus_two(self) -> None:
        when(test_math).add(2, 2).thenReturn(4)
        self.assertEqual(4, test_math.add(2, 2))
        verifyStubbedInvocationsAreUsed()

if __name__ == '__main__':
    unittest.main(verbosity=2)
