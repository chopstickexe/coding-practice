import bisect
import random
import timeit


def remove_items(A, x):
    A.sort()
    index = bisect.bisect_right(A, x)
    return A[index:]


if __name__ == "__main__":
    A = [random.randint(-20, 20) for _ in range(100000000)]
    x = 0
    loop = 10
    result = timeit.timeit("remove_items(A, x)", globals=globals(), number=loop)
    print(f"remove_items(A, x): {result / loop}")
    # $ python -m algs.binary_search
    # remove_items(A, x): 2.492023104199961
