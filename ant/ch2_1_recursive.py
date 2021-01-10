def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)


def fib(n: int) -> int:
    # Slow
    # $ python -m timeit -u msec 'from ant.ch2_1_recursive import fib; fib(10)'
    # 10000 loops, best of 5: 0.0217 msec per loop
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


MAX_N = 1000000
memo = [0 for _ in range(MAX_N)]


def fib2(n: int) -> int:
    # Fast
    # $ python -m timeit -u msec 'from ant.ch2_1_recursive import fib2; fib2(10)'
    # 200000 loops, best of 5: 0.00102 msec per loop
    if n <= 1:
        return n
    if memo[n] != 0:
        # return cached value
        return memo[n]
    else:
        memo[n] = fib(n - 2) + fib(n - 1)
        return memo[n]


def main():
    print(f"10!={fact(10)}")


if __name__ == "__main__":
    main()
