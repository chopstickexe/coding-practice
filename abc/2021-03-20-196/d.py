from collections import deque


def main():
    H, W, A, B = [int(x) for x in input().split()]
    patterns = deque([("o" * (H * W), A)])
    visited = set()
    ans = 0
    while len(patterns) > 0:
        p, a = patterns.pop()
        if p in visited:
            continue
        visited.add(p)
        if a == 0:
            # print("count: " + p)
            ans += 1
            continue
        for i, x in enumerate(p):
            if x == "o":
                if i + W < H * W and p[i + H] == "o":
                    # Place vertically
                    new_p = list(p)
                    new_p[i] = "v"
                    new_p[i + H] = "v"
                    new_p = ''.join(new_p)
                    patterns.append((new_p, a - 1))
                if i + 1 < (i // W + 1) * W and p[i + 1] == "o":
                    # Place holizontally
                    new_p = list(p)
                    new_p[i] = "h"
                    new_p[i + 1] = "h"
                    new_p = ''.join(new_p)
                    patterns.append((new_p, a - 1))
    print(ans)


if __name__ == "__main__":
    main()
