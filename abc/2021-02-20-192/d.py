import math


def main():
    X = int(input())
    M = int(input())

    X_array = [int(x) for x in str(X)]
    d = max(X_array)
    digits = len(X_array)

    max_n = math.ceil((M / X_array[0]) ** (1 / (digits - 1)))
    print(max_n)


if __name__ == "__main__":
    main()
