import time
import threading
from queue import Queue
from src.sensors import latest_temperatures, lock

temperature_averages = {}  # Stores average readings
temp_queue = Queue()  # Queue for temperature processing

def process_temperatures():
    """Processes temperature readings and calculates moving averages."""
    while True:
        with lock:
            if not latest_temperatures:
                continue
            
            avg_temp = sum(latest_temperatures.values()) / len(latest_temperatures)
            temperature_averages['average'] = round(avg_temp, 2)
        
        time.sleep(5)  # Update every 5s
