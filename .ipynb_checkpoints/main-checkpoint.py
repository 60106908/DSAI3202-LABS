from sequential_execution import run_sequential
from threading_execution import run_threads
from multiprocessing_execution import run_processes

def main():
    run_sequential()
    run_threads()
    run_processes()

if __name__ == "__main__":
    main()
