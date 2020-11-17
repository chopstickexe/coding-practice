from typing import List

# Need to use PyPy


def dp(H: int, W: int, S: List[List[str]]) -> int:
    x = [[0 for w in range(0, W)] for h in range(0, H)]
    y = [[0 for w in range(0, W)] for h in range(0, H)]
    z = [[0 for w in range(0, W)] for h in range(0, H)]
    dp = [[0 for w in range(0, W)] for h in range(0, H)]
    for h in range(0, H):
        for w in range(0, W):
            if h == 0 and w == 0:
                dp[h][w] = 1
                continue
            if S[h][w] == "#":
                continue
            if w > 0:
                x[h][w] = x[h][w - 1] + dp[h][w - 1]
            if h > 0:
                y[h][w] = y[h - 1][w] + dp[h - 1][w]
            if w > 0 and h > 0:
                z[h][w] = z[h - 1][w - 1] + dp[h - 1][w - 1]
            dp[h][w] = (x[h][w] + y[h][w] + z[h][w]) % (1000000000 + 7)
    return dp[H - 1][W - 1]


def main():
    H, W = [int(x) for x in input().split()]
    S = ["" for i in range(H)]
    for h in range(H):
        S[h] = input()

    count = dp(H, W, S)
    print(count)


if __name__ == "__main__":
    main()
