# TLE

import sys
from collections import defaultdict

sys.setrecursionlimit(200000) 

def dfs(n, visited, pairs):
    if visited[n]:
        return
    visited[n] = True
    for next in pairs[n]:
        dfs(next, visited, pairs)

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    pairs = defaultdict(list)
    i = 0
    j = N - 1
    while i < j:
        pairs[A[i]].append(A[j])
        pairs[A[j]].append(A[i])
        i += 1
        j -= 1

    ans = len(pairs)
    visited = {k: False for k in pairs.keys()}
    for k in pairs.keys():
        if not visited[k]:
            ans -= 1
            dfs(k, visited, pairs)
    print(ans)


if __name__ == "__main__":
    main()
