import queue
from collections import defaultdict


def main():
    M = int(input())
    g = defaultdict(list)
    for _ in range(M):
        u, v = [int(x) for x in input().split()]
        g[u].append(v)
        g[v].append(u)
    s = ["9"] * 9
    for i, p in enumerate(input().split()):
        s[int(p) - 1] = str(i + 1)
    s = "".join(s)

    q = queue.Queue()
    q.put(s)
    steps = {}
    steps[s] = 0
    ans = -1
    while q.qsize() > 0:
        s = q.get()
        if s == "123456789":
            if ans < 0 or steps[s] < ans:
                ans = steps[s]
            break
        for i in range(0, 9):
            for j in range(i, 9):
                # switch s[i] and s[j] if possible, and queue it
                if s[i] != "9" and s[j] != "9":
                    continue
                if j + 1 not in g[i + 1]:
                    continue
                s_list = list(s)
                temp = s[i]
                s_list[i] = s[j]
                s_list[j] = temp
                t = "".join(s_list)
                if t in steps:
                    continue
                steps[t] = steps[s] + 1
                q.put(t)
    print(ans)


if __name__ == "__main__":
    main()
