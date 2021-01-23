def main():
    N, X = [int(x) for x in input().split()]
    X *= 100
    drank = -1
    for i in range(N):
        V, P = [int(x) for x in input().split()]
        X -= V * P
        if X < 0 and drank < 0:
            drank = i + 1
    print(drank)


if __name__ == "__main__":
    main()
