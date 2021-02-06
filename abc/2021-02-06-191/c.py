def main():
    H, W = [int(x) for x in input().split()]
    S = []
    for h in range(H):
        S.append(input())
    # print(S)
    count = 0
    for h in range(1, H - 1):
        for w in range(1, W - 1):
            # print(f"h={h}, w={w}")
            if S[h][w] == ".":
                continue
            # Check upper-left
            if (S[h - 1][w] == "." and S[h][w - 1] == ".") or (
                S[h - 1][w] == "#" and S[h][w - 1] == "#" and S[h - 1][w - 1] == "."
            ):
                # print(f"ul[{h}][{w}]")
                count += 1
            # Check upper-right
            if (S[h - 1][w] == "." and S[h][w + 1] == ".") or (
                S[h - 1][w] == "#" and S[h][w + 1] == "#" and S[h - 1][w + 1] == "."
            ):
                # print(f"ur[{h}][{w}]")
                count += 1
            # Check lower-left
            if (S[h + 1][w] == "." and S[h][w - 1] == ".") or (
                S[h + 1][w] == "#" and S[h][w - 1] == "#" and S[h + 1][w - 1] == "."
            ):
                # print(f"ll[{h}][{w}]")
                count += 1
            # Check lower-right
            if (S[h + 1][w] == "." and S[h][w + 1] == ".") or (
                S[h + 1][w] == "#" and S[h][w + 1] == "#" and S[h + 1][w + 1] == "."
            ):
                # print(f"lr[{h}][{w}]")
                count += 1
    print(count)


if __name__ == "__main__":
    main()
