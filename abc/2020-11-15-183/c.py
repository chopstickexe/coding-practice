import queue
from dataclasses import dataclass, field
from typing import List

@dataclass
class Route:
    cities: List[int] = field(default_factory=list)
    time: int = 0

def travel(T: List[List[int]], K: int, N: int) -> int:
    count = 0

    q = queue.Queue()
    q.put(Route([0]))
    while not q.empty():
        route = q.get()
        # print(route)
        if len(route.cities) == N:
            # Go back to start
            route.time += T[route.cities[-1]][0]
            if route.time == K:
            # Visited all cities with the time K
                count += 1
            continue
        for n in range(1, N):
            if n not in route.cities:
                new_route = Route(list(route.cities), route.time)
                new_route.time += T[route.cities[-1]][n]
                new_route.cities.append(n)
                q.put(new_route)
    return count

def main():
    N, K = [int(x) for x in input().split()]
    T = [[] for n in range(0, N)]
    for n in range(0, N):
        T[n] = [int(x) for x in input().split()]
    count = travel(T, K, N)
    print(count)

if __name__ == "__main__":
    main()
