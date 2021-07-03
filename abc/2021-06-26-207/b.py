import math


def main():
    A, B, C, D = [int(x) for x in input().split()]
    x = C * D - B
    if x <= 0:
        print(-1)
    else:
        print(int(math.ceil(A / x)))


if __name__ == "__main__":
    main()
