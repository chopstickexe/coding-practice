import heapq
import math
from collections import defaultdict


def main():
    N, M, X, Y = [int(x) for x in input().split()]
    trains = defaultdict(list)
    for m in range(M):
        A, B, T, K = [int(x) for x in input().split()]
        trains[A].append((B, T, K))
        trains[B].append((A, T, K))
    routes = [(0, X)]
    visited = set()
    ans = -1
    while len(routes) > 0:
        cost, city = heapq.heappop(routes)
        if city in visited:
            continue
        # print(f"{city}: {cost}")
        if city == Y:
            ans = cost
            break

        visited.add(city)
        for n_city, n_cost, period in trains[city]:
            if n_city in visited:
                continue
            wait = math.ceil(cost / period) * period - cost
            heapq.heappush(routes, (cost + n_cost + wait, n_city))
    print(ans)


if __name__ == "__main__":
    main()
