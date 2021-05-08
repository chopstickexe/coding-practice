def main():
    N, K = [int(x) for x in input().split()]
    for _ in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
    print(N)


if __name__ == "__main__":
    main()
