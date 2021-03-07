def main():
    N = int(input())
    ans = 0
    for k in range(1, N):
        ans += N / (N - k)
    print(ans)


if __name__ == "__main__":
    main()
