import time
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def find_primes(limit):
    primes = []
    start = time.time()

    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    
    end = time.time()
    print(f"found {len(primes)} primes up to {limit} in {end-start:.2f} seconds")

if __name__ == "__main__":
    find_primes(2_000_000)