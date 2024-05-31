class Solution:
    def getRow(self, rowIndex):
        triangle = []

        for i in range(1, rowIndex + 2):
            row = []
            for j in range(1, i + 1):
                if j == 1 or i == j:
                    row.append(1)
                else:
                    row_last = triangle[-1]
                    row.append(row_last[j - 2] + row_last[j - 1])
            triangle.append(row)

        return triangle[rowIndex]


print(Solution().getRow(3))
