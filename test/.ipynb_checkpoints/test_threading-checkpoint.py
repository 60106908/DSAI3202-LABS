import unittest
from src.threading_sum import parallel_sum_threading

class TestThreadingSum(unittest.TestCase):
    def test_parallel_sum_threading(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = sum(numbers)
        result = parallel_sum_threading(numbers, num_threads=2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
