def main():
    H, W, N = [int(x) for x in input().split()]

    cards = []
    hs = set()
    ws = set()
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        cards.append((A, B))
        hs.add(A)
        ws.add(B)

    hs = sorted(list(hs))
    ws = sorted(list(ws))

    h_map = {old: new + 1 for new, old in enumerate(hs)}
    w_map = {old: new + 1 for new, old in enumerate(ws)}

    ans = []
    for i, (h, w) in enumerate(cards):
        ans.append((h_map[h], w_map[w]))

    for h, w in ans:
        print(f"{h} {w}")


if __name__ == "__main__":
    main()
