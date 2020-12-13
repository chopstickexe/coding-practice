def main():
    n, m, t = [int(x) for x in input().split()]
    prev = 0
    current = n
    empty = False
    for i in range(m):
        A, B = [int(x) for x in input().split()]
        current -= (A - prev)
        # print(f"{A}={current}")
        if current <= 0:
            empty = True
        current += (B - A)
        if current > n:
            current = n
        # print(f"{B}={current}")
        prev = B
    if prev < t:
        current -= (t - prev)
        # print(f"{t}={current}")
    if current > 0 and not empty:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()