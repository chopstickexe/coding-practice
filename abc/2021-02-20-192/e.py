import heapq
import math
import sys
from collections import defaultdict


def main():
    N, M, X, Y = [int(x) for x in input().split()]
    trains = defaultdict(list)
    for m in range(M):
        A, B, T, K = [int(x) for x in input().split()]
        trains[A].append((B, T, K))
        trains[B].append((A, T, K))
    routes = [(X, 0)]
    visited = set()
    ans = sys.maxsize
    while len(routes) > 0:
        city, cost = heapq.heappop(routes)
        # print(f"{city}: {cost}")
        if city == Y and cost < ans:
            ans = cost
            continue
        elif cost > ans:
            # Cannot be the shortest
            continue
        visited.add(city)
        for n_city, n_cost, period in trains[city]:
            if n_city in visited:
                continue
            wait = math.ceil(cost / period) * period - cost
            heapq.heappush(
                routes, (n_city, cost + n_cost + wait)
            )
    print(ans if ans < sys.maxsize else -1)


if __name__ == "__main__":
    main()
