class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if self.binSearch(matrix[i], target):
                return True
        return False

    def binSearch(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            if arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False


def main():
    print(Solution().searchMatrix([[1, 0, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))


if __name__ == '__main__':
    main()
