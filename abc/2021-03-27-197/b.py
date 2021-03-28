def main():
    H, W, X, Y = [int(x) for x in input().split()]
    X = X - 1  # Convert to 0 origin
    Y = Y - 1
    S = []
    for _ in range(H):
        S.append(input())
    ans = 1  # (X, Y) is assured as "."
    for h in range(X - 1, -1, -1):
        if S[h][Y] == "#":
            break
        ans += 1
    for h in range(X + 1, H):
        if S[h][Y] == "#":
            break
        ans += 1
    for w in range(Y - 1, -1, -1):
        if S[X][w] == "#":
            break
        ans += 1
    for w in range(Y + 1, W):
        if S[X][w] == "#":
            break
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
