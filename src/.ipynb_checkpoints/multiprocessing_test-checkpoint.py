import multiprocessing
import time
from computation import generate_and_add_numbers, generate_and_join_letters

def run_processes():
    print("Starting multiprocessing execution")
    start_time = time.time()
    process_numbers = multiprocessing.Process(target=generate_and_add_numbers, args=[int(1e7)])
    process_letters = multiprocessing.Process(target=generate_and_join_letters, args=[int(1e7)])
    process_numbers.start()
    process_letters.start()
    process_numbers.join()
    process_letters.join()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time}s")
