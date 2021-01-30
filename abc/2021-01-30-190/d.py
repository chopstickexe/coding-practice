def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    N = int(input())
    N *= 2
    # Find integers satisfy (2S + M - 1) * M = 2N
    factors_tuples = factorization(N)
    factors = []
    for x in factors_tuples:
        for _ in range(x[1]):
            factors.append(x[0])
    # print(factors)
    num_of_factors = len(factors)

    count = 0
    cache = set()
    for x in range(2 ** num_of_factors):
        M = 1
        for i, c in enumerate(f"{x:b}".zfill(num_of_factors)):
            if c == "1":
                M *= factors[i]
        if M in cache:
            continue
        cache.add(M)
        # print(f"M={M}")
        X = N // M
        # print(f"N={N}")
        if (X + 1 - M) % 2 == 0:
            # print(f"M={M}")
            count += 1
    print(count)


if __name__ == "__main__":
    main()
