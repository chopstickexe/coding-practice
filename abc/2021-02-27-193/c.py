import math


def main():
    N = int(input())
    memo = set()
    for a in range(2, math.floor(math.sqrt(N)) + 1):
        max_b = math.floor(math.log(N, a))
        for b in range(2, max_b + 1):
            memo.add(a ** b)
    print(N - len(memo))


if __name__ == "__main__":
    main()
