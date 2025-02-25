import time
from src.computation import generate_and_add_numbers, generate_and_join_letters


def run_sequential():
    print("Starting sequential execution")
    generate_and_add_numbers(int(1e7))
    generate_and_join_letters(int(1e7))
    print("Sequential execution completed")
