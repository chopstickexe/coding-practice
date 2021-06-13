def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = sorted(A)
    for a, n in zip(A, range(1, N + 1)):
        if a != n:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
