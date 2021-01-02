import sys
from typing import List


def dijkstra(s: int, e: int, cost: List[List[int]]):
    V = len(cost)
    d = [sys.maxsize for _ in range(V)]
    used = [False for _ in range(V)]
    d[s] = 0

    while True:
        v = -1
        # Find a node haven't been used and having the smallest d
        for u in range(0, V):
            if used[u]:
                continue
            if v == -1 or d[u] < d[v]:
                v = u
        if v == -1:
            # Node not found
            return d[e]

        # Pick v
        print(f"Pick {v}")
        used[v] = True

        # Update d of nodes adjacent to v
        for u in range(0, V):
            d[u] = min(d[u], d[v] + cost[v][u])


def main():
    V = 7
    cost = [[sys.maxsize for x in range(V)] for y in range(V)]
    cost[0][1] = 2
    cost[1][0] = 2
    cost[0][2] = 5
    cost[2][0] = 5
    cost[1][2] = 4
    cost[2][1] = 4
    cost[1][3] = 6
    cost[3][1] = 6
    cost[2][3] = 2
    cost[3][2] = 2
    cost[1][4] = 10
    cost[4][1] = 10
    cost[3][5] = 1
    cost[5][3] = 1
    cost[4][5] = 3
    cost[5][4] = 3
    cost[4][6] = 5
    cost[6][4] = 5
    cost[5][6] = 9
    cost[6][5] = 9
    ret = dijkstra(0, 6, cost)
    print(ret)


if __name__ == "__main__":
    main()
