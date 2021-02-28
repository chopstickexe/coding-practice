def main():
    N = int(input())
    ans = 10 ** 9
    for _ in range(N):
        A, P, X = [int(x) for x in input().split()]
        if X - A > 0 and P < ans:
            ans = P
    if ans == 10**9:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
