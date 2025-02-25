import time
from computation import generate_and_add_numbers, generate_and_join_letters

def run_sequential():
    print("Starting sequential execution")
    start_time = time.time()
    generate_and_add_numbers(int(1e7))
    generate_and_join_letters(int(1e7))
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time}s")