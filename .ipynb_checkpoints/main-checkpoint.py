import threading
from src.sensors import simulate_sensor
from src.processing import process_temperatures
from src.display import initialize_display, update_display

def main():
    """Main function to start all threads and initialize display."""
    sensors = [threading.Thread(target=simulate_sensor, args=(i,), daemon=True) for i in range(3)]
    processor = threading.Thread(target=process_temperatures, daemon=True)
    display = threading.Thread(target=update_display, daemon=True)

    # Start all threads
    for thread in sensors:
        thread.start()
    processor.start()
    display.start()

    initialize_display()

    # Keep the main thread alive
    while True:
        pass

if __name__ == "__main__":
    main()
