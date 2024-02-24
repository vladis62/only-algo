class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        s = 0
        for i in range(1, n + 1):
            s += i
        return s - sum(nums)


def main():
    Solution().missingNumber([3, 0, 1])


if __name__ == '__main__':
    main()
