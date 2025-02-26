import random
import time
import threading

latest_temperatures = {}  # Stores latest readings
lock = threading.RLock()  # Synchronization lock

def simulate_sensor(sensor_id):
    """Simulates a temperature sensor and updates the global dictionary."""
    while True:
        temp = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temp
        time.sleep(1)  # Update every 1s
