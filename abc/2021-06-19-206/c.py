from collections import defaultdict


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    uniq_a = defaultdict(list)
    for i, a in enumerate(A):
        uniq_a[a].append(i)
    dup = 0
    for a in uniq_a.keys():
        m = len(uniq_a[a])
        dup += (m - 1) * m // 2
    print((N - 1) * N // 2 - dup)


if __name__ == "__main__":
    main()
