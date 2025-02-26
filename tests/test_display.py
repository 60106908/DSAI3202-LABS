import unittest
from src.display import initialize_display

class TestDisplay(unittest.TestCase):
    def test_initialize_display(self):
        self.assertIsNone(initialize_display())

if __name__ == '__main__':
    unittest.main()
