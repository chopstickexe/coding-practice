def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    A_sum = 0
    for i in range(N):
        a = A[i]
        ans += (N - 1) * (a ** 2)
        ans -= 2 * a * A_sum
        A_sum += a
    print(ans)


if __name__ == "__main__":
    main()
