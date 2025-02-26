import os
import time
import threading
from src.sensors import latest_temperatures, lock
from src.processing import temperature_averages

def initialize_display():
    """Prints the initial display layout."""
    print("\nCurrent Temperatures:")
    print("\nLatest Temperatures:", " ".join(f"Sensor {i}: --°C" for i in range(3)))
    print("\nSensor Averages: --°C\n")

def update_display():
    """Updates the display in place without clearing the console."""
    while True:
        with lock:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clears console
            
            print("\nCurrent Temperatures:")
            for sensor, temp in latest_temperatures.items():
                print(f"Sensor {sensor}: {temp}°C", end="   ")
            
            print("\n\nAverage Temperature:", temperature_averages.get('average', "--"), "°C\n")
        
        time.sleep(5)  # Update every 5s
