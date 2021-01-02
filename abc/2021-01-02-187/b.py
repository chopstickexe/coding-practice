def main():
    N = int(input())
    x = [0 for _ in range(N)]
    y = [0 for _ in range(N)]
    for i in range(N):
        x[i], y[i] = [int(x) for x in input().split()]

    count = 0
    for i in range(N):
        for j in range(i, N):
            if x[j] == x[i]:
                continue
            g = (y[j] - y[i]) / (x[j] - x[i])
            if g >= -1 and g <= 1:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
