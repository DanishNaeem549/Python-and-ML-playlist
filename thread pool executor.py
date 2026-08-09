from concurrent.futures import ThreadPoolExecutor
import time

def square(n):
    print(f"Calculating square of {n}")
    time.sleep(1)
    return n * n


numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, numbers)

for result in results:
    print(result)