class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        history = set()
        duplicate = 0
        actual_sum = 0

        for num in nums:
            if num in history:
                duplicate = num
            history.add(num)
            actual_sum += num

        return [duplicate, expected_sum - (actual_sum - duplicate)]


def main():
    print(Solution().findErrorNums([1, 2, 2, 4]))


if __name__ == '__main__':
    main()
