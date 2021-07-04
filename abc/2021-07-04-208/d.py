def main():
    N, M = [int(x) for x in input().split()]
    d = [[10 ** 6 * 400 * 400] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        d[i][i] = 0
    for _ in range(M):
        A, B, C = [int(x) for x in input().split()]
        d[A][B] = C
    ans = 0
    for k in range(1, N + 1):
        d_next = [[10 ** 6] * (N + 1) for _ in range(N + 1)]
        for s in range(1, N + 1):
            for t in range(1, N + 1):
                d_next[s][t] = min(d[s][t], d[s][k] + d[k][t])
                if d_next[s][t] < 10 ** 6 * 400 * 400:
                    # found a route
                    ans += d_next[s][t]
        d = d_next
    print(ans)


if __name__ == "__main__":
    main()
