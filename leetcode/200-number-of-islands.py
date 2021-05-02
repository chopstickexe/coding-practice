# https://leetcode.com/problems/number-of-islands/

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        m = len(grid)
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()

        def _dep():
            i, j = queue.popleft()
            if visited[i][j]:
                return
            visited[i][j] = True
            if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == "1":
                queue.append((i - 1, j))
            if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == "1":
                queue.append((i, j - 1))
            if j + 1 < n and not visited[i][j + 1] and grid[i][j + 1] == "1":
                queue.append((i, j + 1))
            if i + 1 < m and not visited[i + 1][j] and grid[i + 1][j] == "1":
                queue.append((i + 1, j))
            # print(queue)

        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    # DFS from (i, j) and visit all "1"s connected to the cell (those will be one island)
                    queue.append((i, j))
                    while len(queue) > 0:
                        _dep()
                    count += 1
        return count
