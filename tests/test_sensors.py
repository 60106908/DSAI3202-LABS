import unittest
from src.sensors import simulate_sensor, latest_temperatures

class TestSensor(unittest.TestCase):
    def test_sensor_update(self):
        simulate_sensor(0)
        self.assertIn(0, latest_temperatures)

if __name__ == '__main__':
    unittest.main()
