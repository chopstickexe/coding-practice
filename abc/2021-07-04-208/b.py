def main():
    coins = []
    last = 1
    max_p = 10 ** 7
    for i in range(1, max_p):
        x = last * i
        if x > max_p:
            break
        coins.append(x)
        last = x
    # print(coins)

    P = int(input())
    ans = 0
    for x in coins[::-1]:
        if x > P:
            continue
        ans += P // x
        P = P % x
    print(ans)


if __name__ == "__main__":
    main()
