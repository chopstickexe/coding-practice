from typing import Dict, List, Tuple


def get_input() -> Tuple[int, int, Dict[int, List[int]]]:
    N, M = [int(x) for x in input().split()]
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = [int(x) for x in input().split()]
        graph[A].append(B)
        graph[B].append(A)
    return N, M, graph


def list_connected(
    start: int, graph: Dict[int, List[int]], visited: List[bool]
) -> List[int]:
    """Get a set of nodes in the given graph connected by edges.
    Note that the returned nodes are ordered from the root (start) to leafs.
    """
    ret = []

    def dfs(i: int):
        ret.append(i)
        visited[i] = True
        for neighbor in graph[i]:
            if visited[neighbor]:
                continue
            dfs(neighbor)

    dfs(start)
    return ret


def color(nodes: List[int], graph: Dict[int, List[int]], N: int) -> int:
    """Count possible coloring patterns of the given nodes"""

    def _color(i, pattern):
        """Given a coloring pattern having 0-(i-1)th elements of nodes are colored,
        count a number of patterns for elements of ith and after.
        Return 0 if no possible pattern is available, and 1 if it comes to the end.
        """
        if i == len(nodes):
            # Succcessfully colored all nodes
            # print(pattern)
            return 1

        n = nodes[i]
        ret = 0
        for c in [1, 2, 3]:
            # Try each color
            def _ok(c):
                for neighbor in graph[n]:
                    if pattern[neighbor] == c:
                        return False
                return True

            if not _ok(c):
                continue
            # Try coloring this node as c
            pattern[n] = c
            # Get a number of possible patterns after this node (get sum because these are "OR" options)
            ret += _color(i + 1, pattern)
            # Back to initial before trying another
            pattern[n] = 0
        return ret

    pattern = [0 for _ in range(N + 1)]
    return _color(0, pattern)


def main():
    N, M, graph = get_input()
    visited = [False for _ in range(N + 1)]
    ans = 1
    for i in range(1, N + 1):
        if visited[i]:
            continue
        connected = list_connected(i, graph, visited)
        # print(connected)
        ans *= color(connected, graph, N)
    print(ans)


if __name__ == "__main__":
    main()
