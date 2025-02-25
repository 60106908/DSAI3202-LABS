import random

def generate_and_add_numbers(n: int = 1000):
    """Generates n random numbers and returns their sum."""
    return sum(random.randint(0, 1000000) for _ in range(n))

def generate_and_join_letters(n: int = 1000):
    """Generates n random ASCII characters and joins them into a string."""
    return ''.join(chr(random.randint(33, 126)) for _ in range(n))
