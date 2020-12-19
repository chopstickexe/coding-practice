def main():
    h, w = [int(x) for x in input().split()]
    A = [[0 for x in range(0, w)] for y in range(0, h)]
    for y in range(0, h):
        A[y] = [int(x) for x in input().split()]

    min_a = 100
    for y in range(0, h):
        for x in range(0, w):
            if A[y][x] < min_a:
                min_a = A[y][x]

    sum_a = 0
    for y in range(0, h):
        for x in range(0, w):
            sum_a += A[y][x] - min_a
    print(sum_a)


if __name__ == "__main__":
    main()
