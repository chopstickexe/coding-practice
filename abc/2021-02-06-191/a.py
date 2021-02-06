def main():
    V, T, S, D = [int(x) for x in input().split()]
    start = V * T
    end = V * S
    if D < start or end < D:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
