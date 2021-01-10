import sys
from typing import List


def dijkstra(s: int, e: int, cost: List[List[int]]):
    # O(|V|^2)
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


def parse_input():
    V, E = [int(x) for x in input().split()]
    S, G = [int(x) for x in input().split()]
    cost = [[sys.maxsize for x in range(V)] for y in range(V)]
    for _ in range(0, E):
        i, j, c = [int(x) for x in input().split()]
        cost[i][j] = c
        cost[j][i] = c  # undirected graph
    return V, E, S, G, cost


def main():
    V, E, S, G, cost = parse_input()
    ret = dijkstra(S, G, cost)
    print(ret)


if __name__ == "__main__":
    main()
