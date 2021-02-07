import heapq
import sys
from collections import defaultdict


def dijkstra(start, N, routes):
    """Find shortest pathes to other N - 1 cities from the start city (1 ... N).
    O((N + M)logN) for N (Number of nodes) and M (Number of edges) """
    cost = [sys.maxsize] * (N + 1)
    visited = [False] * (N + 1)  # Avoid loop
    q = [(0, start)]  # (distance, node)
    cost[start] = 0
    while q:  # O(N)
        current_c, current_n = heapq.heappop(q)  # O(logN) (O(NlogN) for total pop)
        if current_c > cost[current_n]:
            # Won't be the shortest
            continue
        visited[current_n] = True
        for n, c in routes[current_n]:  # O(M)
            if not visited[n] and cost[n] > c + current_c:
                # Update the shortest path (minimum cost)
                cost[n] = c + current_c
                heapq.heappush(q, (cost[n], n))  # O(logN) (O(MlogN) for total push)
    return cost


def main():
    N, M = [int(x) for x in input().split()]
    routes = defaultdict(list)
    for _ in range(M):
        A, B, C = [int(x) for x in input().split()]
        routes[A].append((B, C))

    costs = [[sys.maxsize] * (N + 1)]
    # oneway
    for n in range(1, N + 1):
        costs.append(dijkstra(n, N, routes))
    # print(costs)

    # Find the shortest round path from i to i
    for i in range(1, N + 1):
        ans = sys.maxsize
        # search direct round routes (could be more than 2)
        if i in routes:
            for n, c in routes[i]:
                if i == n:
                    ans = min(ans, c)
        # search standard round routes via another stop over city
        for stopover in range(1, N + 1):
            if stopover == i:
                continue
            ans = min(ans, costs[i][stopover] + costs[stopover][i])
        print(ans if ans < sys.maxsize else -1)


if __name__ == "__main__":
    main()
