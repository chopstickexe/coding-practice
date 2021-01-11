def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for a, b in zip(A, B):
        ans += a * b
    if ans == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
