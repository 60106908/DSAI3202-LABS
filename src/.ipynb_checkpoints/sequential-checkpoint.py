import time

def sequential_sum(n):
    """Calculates sum of numbers from 1 to n sequentially."""
    start_time = time.time()
    total = sum(range(1, n + 1))
    end_time = time.time()
    
    execution_time = end_time - start_time
    return total, execution_time

if __name__ == "__main__":
    n = 10**7  # Change this number for testing
    total, exec_time = sequential_sum(n)
    print(f"Sequential Sum: {total}")
    print(f"Execution Time: {exec_time:.6f} seconds")
