from functools import lru_cache
import time
import sys

# Increase recursion limit to handle large Fibonacci numbers
sys.setrecursionlimit(2000)  # Adjust as necessary for your use case

# Function to calculate the nth Fibonacci number
@lru_cache(maxsize=1000)  # Cache up to 1000 results
def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative integers")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    n = 999  # Example large Fibonacci number
    start_time = time.time()
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")

    # Try the same computation again, demonstrating cache effectiveness
    start_time = time.time()
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    print(f"Time taken (cached): {time.time() - start_time:.4f} seconds")
    print("completed")
