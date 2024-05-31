class Solution(object):
    def largestLocal(self, grid):
        result = []

        def max_in_matrix(row, col):
            max_matrix = float('-inf')
            save_col = col
            for i in range(3):
                for j in range(3):
                    max_matrix = max(max_matrix, grid[row][col])
                    col += 1
                col = save_col
                row += 1

            return max_matrix

        for i in range(len(grid) - 2):
            inner_result = []
            for j in range(len(grid[i]) - 2):
                inner_result.append(max_in_matrix(i, j))
            result.append(inner_result)

        return result


print(Solution().largestLocal(grid=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
