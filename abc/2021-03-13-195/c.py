def main():
    N = int(input())
    digits = len(str(N))
    ans = (N - (10 ** (digits - 1) - 1)) * ((digits - 1) // 3)
    for d in range(4, digits):
        commas = 10 ** (d - 1) * 9 * ((d - 1) // 3)
        ans += commas
    print(ans)


if __name__ == "__main__":
    main()
