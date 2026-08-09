from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n


numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)