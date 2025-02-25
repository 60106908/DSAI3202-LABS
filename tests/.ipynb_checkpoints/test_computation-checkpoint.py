import unittest
from src.computation import generate_and_add_numbers, generate_and_join_letters

class TestComputation(unittest.TestCase):
    def test_generate_and_add_numbers(self):
        result = generate_and_add_numbers(100)
        self.assertIsInstance(result, int)
    
    def test_generate_and_join_letters(self):
        result = generate_and_join_letters(100)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()

# tests/test_threading_test.py
import unittest
from src.threading_test import run_threads

class TestThreading(unittest.TestCase):
    def test_run_threads(self):
        run_threads()

if __name__ == "__main__":
    unittest.main()