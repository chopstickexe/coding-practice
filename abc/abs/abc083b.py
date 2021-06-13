def main():
    N, A, B = [int(x) for x in input().split()]
    ans = 0
    for n in range(1, N + 1):
        sum_n = sum([int(x) for x in str(n)])
        if A <= sum_n and sum_n <= B:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
