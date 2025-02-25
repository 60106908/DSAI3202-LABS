import unittest
from src.performance import run_sequential

class TestPerformance(unittest.TestCase):
    def test_run_sequential(self):
        run_sequential()

if __name__ == "__main__":
    unittest.main()