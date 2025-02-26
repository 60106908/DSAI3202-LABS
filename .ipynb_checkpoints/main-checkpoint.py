from src.sequential import sequential_sum
from src.threading_sum import threaded_sum
from src.multiprocessing_sum import multiprocessing_sum

def main():
    n = 10**7  # Large number for testing

    print("\n🔹 Running Sequential Version...")
    seq_total, seq_time = sequential_sum(n)
    print(f"Result: {seq_total}, Execution Time: {seq_time:.6f} sec\n")

    print("\n🔹 Running Threading Version...")
    thr_total, thr_time = threaded_sum(n)
    print(f"Result: {thr_total}, Execution Time: {thr_time:.6f} sec\n")

    print("\n🔹 Running Multiprocessing Version...")
    mp_total, mp_time = multiprocessing_sum(n)
    print(f"Result: {mp_total}, Execution Time: {mp_time:.6f} sec\n")

    # Speedup and Efficiency Calculations
    speedup_threading = seq_time / thr_time
    speedup_multiprocessing = seq_time / mp_time

    print("\n📊 Performance Metrics:")
    print(f"Speedup (Threading): {speedup_threading:.2f}")
    print(f"Speedup (Multiprocessing): {speedup_multiprocessing:.2f}")

if __name__ == "__main__":
    main()
