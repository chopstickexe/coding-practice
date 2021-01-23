from functools import lru_cache
import timeit


def fib_memo(n: int):
    # https://qiita.com/dovedove/items/3456c4f317a5c680f437#%E3%83%A1%E3%83%A2%E5%8C%96%E3%81%AE%E5%AE%9F%E8%A3%85
    memo = [-1 for _ in range(n + 1)]

    def _fib(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif memo[n] > 0:
            return memo[n]
        else:
            memo[n] = _fib(n - 1) + _fib(n - 2)
            return memo[n]

    return _fib(n)


@lru_cache(maxsize=None)
def fib_lru_cache(n: int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_lru_cache(n - 1) + fib_lru_cache(n - 2)


if __name__ == "__main__":
    loop = 10
    result = timeit.timeit('fib_memo(40)', globals=globals(), number=loop)
    print(f'fib_memo(40): {result / loop}')
    result = timeit.timeit('fib_lru_cache(40)', globals=globals(), number=loop)
    print(f'fib_lru_cache(40): {result / loop}')
