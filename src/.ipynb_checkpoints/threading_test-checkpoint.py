import threading
import time
from src.computation import generate_and_add_numbers, generate_and_join_letters

def run_threads():
    print("Starting threading execution")
    start_time = time.time()
    thread_numbers = threading.Thread(target=generate_and_add_numbers, args=[int(1e7)])
    thread_letters = threading.Thread(target=generate_and_join_letters, args=[int(1e7)])
    thread_numbers.start()
    thread_letters.start()
    thread_numbers.join()
    thread_letters.join()
    end_time = time.time()
    print(f"Threading execution time: {end_time - start_time}s")