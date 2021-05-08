# https://qiita.com/masayoshi361/items/0be4bce77783b6013b34


def main():
    N, M = [int(x) for x in input().split()]
    edge = [0] * N
    for i in range(M):
        x, y = [int(x) for x in input().split()]
        edge[x - 1] |= 1 << (y - 1)
        print(f"i = {i}, edge = {edge}")
    dp = [0] * (1 << N)
    dp[0] = 1
    print(f"dp = {dp}")
    for s in range(1, 1 << N):
        for i in range(N):
            if ((s >> i) & 1) and (not (edge[i] & s)):
                print(f"s ^ (1 << i) = {s ^ (1 << i)}")
                dp[s] += dp[s ^ (1 << i)]
            print(
                f"s = {s} ({s:b}), i = {i}, ((s >> i) & 1) and (not (edge[i] & s)) = {((s >> i) & 1) and (not (edge[i] & s))}, dp = {dp}"
            )
    print(dp[-1])


if __name__ == "__main__":
    main()
