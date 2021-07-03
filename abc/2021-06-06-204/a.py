def main():
    x, y = [int(x) for x in input().split()]
    dashita = [False for _ in range(3)]
    dashita[x] = True
    dashita[y] = True
    if sum(dashita) == 2:
        ans = [i for i in range(3) if not dashita[i]]
        print(ans[0])
    else:
        print(x)


if __name__ == "__main__":
    main()
