from src.performance import run_sequential
from src.threading_test import run_threads
from src.multiprocessing_test import run_processes
from src.computation import generate_and_add_numbers, generate_and_join_letters
import threading
import multiprocessing

import time

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

def run_sequential():
    print("Starting sequential execution")
    start_time = time.time()
    generate_and_add_numbers(int(1e7))
    generate_and_join_letters(int(1e7))
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time}s")
def main():
    run_sequential()
    run_threads()
    run_processes()

if __name__ == "__main__":
    main()
