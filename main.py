import sys
import os
import threading
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Add current directory to path

from src.sensors import simulate_sensor
from src.processing import process_temperatures
from src.display import initialize_display, update_display

import threading
import time
from src.sensors import simulate_sensor, latest_temperatures
from src.processing import process_temperatures, temperature_averages

def print_results():
    """Prints temperature readings and averages continuously in a scrolling format."""
    while True:
        with threading.RLock():  # Ensure safe access to shared data
            print("\nCurrent Temperatures:")
            for sensor, temp in latest_temperatures.items():
                print(f"Sensor {sensor}: {temp}°C")
            
            avg_temp = temperature_averages.get('average', "--")
            print(f"\nAverage Temperature: {avg_temp}°C")
            print("=" * 40)  # Separator for readability
        
        time.sleep(5)  # Update every 5 seconds

def main():
    """Main function to start all threads and print results."""
    sensors = [threading.Thread(target=simulate_sensor, args=(i,), daemon=True) for i in range(3)]
    processor = threading.Thread(target=process_temperatures, daemon=True)
    display = threading.Thread(target=print_results, daemon=True)

    # Start all threads
    for thread in sensors:
        thread.start()
    processor.start()
    display.start()

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
