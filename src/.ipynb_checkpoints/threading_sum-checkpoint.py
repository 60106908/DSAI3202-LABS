import threading
import time

def partial_sum(start, end, result, index):
    """Calculates partial sum in a given range."""
    result[index] = sum(range(start, end + 1))

def threaded_sum(n, num_threads=4):
    """Parallel summation using threads."""
    start_time = time.time()
    step = n // num_threads
    result = [0] * num_threads
    threads = []

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i != num_threads - 1 else n
        thread = threading.Thread(target=partial_sum, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(result)
    end_time = time.time()

    execution_time = end_time - start_time
    return total, execution_time

if __name__ == "__main__":
    n = 10**7
    total, exec_time = threaded_sum(n)
    print(f"Threaded Sum: {total}")
    print(f"Execution Time: {exec_time:.6f} seconds")
