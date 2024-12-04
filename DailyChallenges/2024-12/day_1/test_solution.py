import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [10, 2, 5, 3]
        result = self.solution.checkIfExist(arr)
        self.assertTrue(result)

    def test_example_2(self):
        arr = [3, 1, 7, 11]
        result = self.solution.checkIfExist(arr)
        self.assertFalse(result)

    def test_empty_list(self):
        arr = []
        result = self.solution.checkIfExist(arr)
        self.assertFalse(result)

    def test_single_element(self):
        arr = [1]
        result = self.solution.checkIfExist(arr)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()