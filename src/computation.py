import random
import random

def generate_and_add_numbers(n=1000):
    """Generates 'n' random numbers and returns their sum."""
    numbers = [random.randint(1, 100) for _ in range(n)]
    return sum(numbers)

def generate_and_join_letters(n: int = 1000):
    """Generates n random ASCII characters and joins them into a string."""
    return ''.join(chr(random.randint(33, 126)) for _ in range(n))
