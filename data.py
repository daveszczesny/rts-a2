import time
import random

def generate_and_sort(size):
    data = [random.randint(0, 10**6) for _ in range(size)]
    start = time.time()

    data.sort()

    end = time.time()
    print(f"sorted {size} numbers in {end-start:.2f} seconds")

if __name__ == "__main__":
    generate_and_sort(10**6)