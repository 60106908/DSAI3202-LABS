import unittest
from src.multiprocessing_sum import parallel_sum_multiprocessing

class TestMultiprocessingSum(unittest.TestCase):
    def test_parallel_sum_multiprocessing(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = sum(numbers)
        result = parallel_sum_multiprocessing(numbers, num_processes=2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
