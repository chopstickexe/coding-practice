def to_int(x):
    ans = 0
    for i, n in enumerate(x):
        ans += 10 ** (len(x) - i - 1) * n
    return ans


def main():
    N, K = [int(x) for x in input().split()]
    a = [int(x) for x in str(N)]
    for i in range(K):
        g1 = to_int(sorted(a, reverse=True))
        g2 = to_int(sorted(a))
        a = [int(x) for x in str(g1 - g2)]
    print(to_int(a))


if __name__ == "__main__":
    main()
