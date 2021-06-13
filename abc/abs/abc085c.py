def main():
    N, Y = [int(x) for x in input().split()]
    Y = Y // 1000
    for an in range(N + 1, -1, -1):
        if an * 10 > Y:
            continue
        for bn in range(N + 1 - an, -1, -1):
            if an * 10 + bn * 5 > Y:
                continue
            cn = N - an - bn
            if an * 10 + bn * 5 + cn * 1 == Y:
                print(f"{an} {bn} {cn}")
                return
    print("-1 -1 -1")


if __name__ == "__main__":
    main()
