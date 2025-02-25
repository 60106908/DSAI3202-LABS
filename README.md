#####lab2 ####
This lab focuses on implementing parallel programs using threads and processes in Python:

    Build a program using threads in Python.
    Build a program using processes in Python.
    Measure and compare performance across different execution models.
****Tasks***
 The Sequential Case
  Implement two functions:
  A function that generates 1000 random characters and joins them into a string.
  A function that generates 1000 random numbers and sums them.
  Measure the execution time of both functions when executed sequentially.
2.b. Threading
  Run each function in a separate thread and time the execution.
  Advanced Task: Run two threads per function and observe performance changes.
2.c. Processes
  Run each function in a separate process and time the execution.
  Advanced Task: Run two processes per function and analyze the results.
2.d. Performance Analysis
  For each case (sequential, threads, and processes), compute:
  *Speedup
  *Efficiency
  where P is the number of threads/processes.
  Speedup using Amdahl’s Law
  where f is the parallelizable portion of the code.
  Speedup using Gustafson’s Law
2.e.Conclusions

    Analyze the performance results.
    Compare threading vs. multiprocessing.
    Discuss whether using more threads/processes always leads to better performance.
