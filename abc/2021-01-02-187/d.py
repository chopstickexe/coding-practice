def main():
    N = int(input())

    towns = [0 for _ in range(N)]
    result = 0
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        towns[i] = 2 * A + B
        result -= A  # Lost when not visiting this town
    towns.sort(reverse=True)
    # print(towns)
    for i in range(N):
        result += towns[i]
        if result > 0:
            print(i + 1)
            return
    print(N)


if __name__ == "__main__":
    main()
