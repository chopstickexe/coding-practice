def make_divisors(n):
    lowers, uppers = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            # print(f"lower->{i}")
            lowers.append(i)
            x = n // i
            if x != i:
                # print(f"upper->{x}")
                uppers.append(x)
        i += 1
    return lowers + uppers[::-1]


def main():
    N = int(input())
    N *= 2
    # Find integers satisfy (2S + M - 1) * M = 2N
    divisors = make_divisors(N)
    # print(divisors)

    count = 0
    for M in divisors:
        X = N // M
        if (X - (M - 1)) % 2 == 0:
            # print(f"M={M}, S={(X - (M - 1)) / 2}")
            count += 1
    print(count)


if __name__ == "__main__":
    main()
