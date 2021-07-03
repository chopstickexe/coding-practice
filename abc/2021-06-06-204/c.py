import sys
from collections import defaultdict

sys.setrecursionlimit(10000)


def main():
    N, M = [int(x) for x in input().split()]
    edges = defaultdict(list)
    for _ in range(M):
        A, B = [int(x) for x in input().split()]
        edges[A].append(B)

    ans = 0
    for i in range(1, N + 1):
        visited = [False] * (N + 1)

        def _dfs(v: int):
            if visited[v]:
                return
            visited[v] = True
            for vv in edges[v]:
                _dfs(vv)

        _dfs(i)
        ans += sum(visited)
    print(ans)


if __name__ == "__main__":
    main()
