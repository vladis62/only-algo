class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        if maxMove <= 0:
            return 0

        MOD = 10 ** 9 + 7

        dp = [[0] * n for _ in range(n)]
        dp[startRow][startColumn] = 1
        result = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for direction in directions:
                        ni, nj = i + direction[0], j + direction[1]
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            result = (result + dp[i][j]) % MOD
                        else:
                            temp[ni][nj] = (temp[ni][nj] + dp[i][j]) % MOD
            dp = temp

        return result
