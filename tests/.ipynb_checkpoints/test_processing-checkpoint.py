import unittest
from src.processing import process_temperatures, temperature_averages

class TestProcessing(unittest.TestCase):
    def test_average_calculation(self):
        process_temperatures()
        self.assertIn('average', temperature_averages)

if __name__ == '__main__':
    unittest.main()
