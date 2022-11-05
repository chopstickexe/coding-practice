class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        print(n)
        output = True
        for i in range(0, n):
            for j in range(0, n):
                if i == j or (i + j) == (n - 1):
                    if grid[i][j] == 0:
                        output = False
                        break
                elif grid[i][j] != 0:
                    output = False
                    break
            if not output:
                break
        return output
