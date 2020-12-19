def main():
    n = int(input())
    A = [int(x) for x in input().split()]
    A.sort(reverse=True)
    ans = 0
    for i, a in enumerate(A):
        ans += (n - (i + 1) - i) * a
    print(ans)


if __name__ == "__main__":
    main()
