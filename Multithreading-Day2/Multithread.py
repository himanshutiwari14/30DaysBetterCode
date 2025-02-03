import threading
import time
import math  # Using math.factorial for larger number calculations

def factorial(n):
    """Function to calculate factorial of a given number."""
    start = time.time()
    result = math.factorial(n)
    end = time.time()
    print(f"Factorial of {n} is calculated in {end - start:.4f} seconds.")

# List of larger numbers to compute factorial
numbers = [100000, 120000, 130000, 150000]

### Without Multithreading ###
start_time = time.time()  # Start time
for num in numbers:
    factorial(num)  # Compute factorial sequentially
end_time = time.time()  # End time
print(f"\nTime taken without threading: {end_time - start_time:.4f} seconds\n")

### With Multithreading ###
threads = []
start_time = time.time()  # Start time
for num in numbers:
    thread = threading.Thread(target=factorial, args=(num,))
    threads.append(thread)
    thread.start()  # Start the thread

# Waiting for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()  # End time
print(f"\nTime taken with threading: {end_time - start_time:.4f} seconds")
