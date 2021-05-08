def main():
    N = int(input())
    A = [int(x) % 200 for x in input().split()]  # Take mod 200
    groups = {}
    for a in A:
        if a not in groups:
            groups[a] = 1
        else:
            groups[a] += 1
    ans = 0
    for k, v in groups.items():
        if v == 1:
            continue
        ans += v * (v - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
