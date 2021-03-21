import math


def main():
    A, B, W = [int(x) for x in input().split()]
    W *= 1000

    upper = int(math.floor(W / A))
    lower = int(math.ceil(W / B))
    if lower > upper:
        print("UNSATISFIABLE")
    else:
        print(lower, upper)


if __name__ == "__main__":
    main()
