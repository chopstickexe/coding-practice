def main():
    x = [[], []]
    for i in range(0, 2):
        x[i] = [int(x) for x in input().split()]
    ans = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    print(ans)


if __name__ == "__main__":
    main()
