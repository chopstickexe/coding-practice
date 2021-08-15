import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
from typing import Dict, List, Set


def main():
    N = int(input())

    cities = defaultdict(list)
    for _ in range(1, N):
        A, B = [int(x) for x in input().split()]
        cities[A].append(B)
        cities[B].append(A)
    
    for c, ns in cities.items():
        cities[c] = sorted(ns)
    
    history = []
    def _dfs(cur, prev):
        history.append(cur)
        for n in cities.get(cur):
            if n != prev:
                _dfs(n, cur)  # visit the neighbour
                history.append(cur)  # go back to the current
        
    _dfs(1, -1)
    print(' '.join([str(x) for x in history]))


if __name__ == "__main__":
    main()
