import multiprocessing
import time

def partial_sum(start, end, queue):
    """Calculates partial sum and puts result in queue."""
    queue.put(sum(range(start, end + 1)))

def multiprocessing_sum(n, num_processes=4):
    """Parallel summation using processes."""
    start_time = time.time()
    step = n // num_processes
    queue = multiprocessing.Queue()
    processes = []

    for i in range(num_processes):
        start = i * step + 1
        end = (i + 1) * step if i != num_processes - 1 else n
        process = multiprocessing.Process(target=partial_sum, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total = sum(queue.get() for _ in range(num_processes))
    end_time = time.time()

    execution_time = end_time - start_time
    return total, execution_time

if __name__ == "__main__":
    n = 10**7
    total, exec_time = multiprocessing_sum(n)
    print(f"Multiprocessing Sum: {total}")
    print(f"Execution Time: {exec_time:.6f} seconds")
