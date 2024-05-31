class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0

        def calc(grid, i, j):
            max_perimeter = 4
            if i > 0 and grid[i - 1][j] == 1:
                max_perimeter -= 1
            if i < (len(grid) - 1) and grid[i + 1][j] == 1:
                max_perimeter -= 1
            if j > 0 and grid[i][j - 1] == 1:
                max_perimeter -= 1
            if j < (len(grid[i]) - 1) and grid[i][j + 1]:
                max_perimeter -= 1
            return max_perimeter

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += calc(grid, i, j)

        return perimeter


print(Solution().islandPerimeter(grid=[[1]]))
