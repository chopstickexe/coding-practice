def main():
    N = int(input())
    areas = []

    for i in range(N):
        t, l, r = [int(x) for x in input().split()]

        l *= 10
        if t == 3 or t == 4:
            l += 1  # Doesn't include l

        r *= 10
        if t == 2 or t == 4:
            r -= 1  # Doesn't include r

        areas.append((l, r))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if max(areas[i][0], areas[j][0]) <= min(areas[i][1], areas[j][1]):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
