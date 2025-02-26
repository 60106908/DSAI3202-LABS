# Lab 3 - Data Parallel Model

## Objectives
- Implement summation using **sequential**, **threading**, and **multiprocessing** approaches.
- Compare execution times and compute speedup & efficiency.

## Results Comparison (Example Outputs)
| Implementation | Execution Time (seconds) |
|---------------|----------------------|
| Sequential    | 1.50                 |
| Threading     | 0.90                 |
| Multiprocessing | 0.45               |

## Performance Analysis
- **Speedup (Threading)** = Sequential Time / Threading Time
- **Speedup (Multiprocessing)** = Sequential Time / Multiprocessing Time

## Questions & Answers

### 1. How does execution time change from sequential → threading → multiprocessing?
- Threading **reduces execution time** but still runs on a **single CPU core**.
- Multiprocessing **fully utilizes multiple CPU cores**, leading to **better speedup**.

### 2. Compute:
#### a) **Speedup**
- `Speedup = Sequential Time / Parallel Time`
- **Example:**
  - Speedup (Threading) = `1.50 / 0.90 = 1.67`
  - Speedup (Multiprocessing) = `1.50 / 0.45 = 3.33`

#### b) **Efficiency**
- `Efficiency = Speedup / Number of Threads or Processes`
- **Example:**
  - Efficiency (Threading) = `1.67 / 4 = 0.42`
  - Efficiency (Multiprocessing) = `3.33 / 4 = 0.83`

#### c) **Amdahl’s Law**
- `Speedup = 1 / (S + (1-S)/P)`
  - Where **S** = Serial Fraction, **P** = Number of Processors.

#### d) **Gustafson’s Law**
- `Speedup = S + P * (1-S)`

### 3. Performance Differences between Threading & Multiprocessing?
- **Threading** uses shared memory → **slower** due to GIL.
- **Multiprocessing** uses separate processes → **faster**.

### 4. Challenges Faced & Solutions
- **GIL Limitation**: Used multiprocessing for full CPU usage.
- **Race Conditions**: Used locks in threading.
- **Memory Overhead**: Used a queue to manage process results.

### 5. When to use Threading vs. Multiprocessing?
- **Threading**: When tasks are **I/O-bound** (e.g., web scraping).
- **Multiprocessing**: When tasks are **CPU-bound** (e.g., heavy computations).

---
