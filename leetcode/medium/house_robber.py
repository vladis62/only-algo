class Solution(object):
    def rob(self, nums):
        results = [0 for _ in range(len(nums) + 3)]

        for i in range(len(nums) - 1, -1, -1):
            results[i] = nums[i] + max(results[i + 2], results[i + 3])
        return max(results)


def main():
    print(Solution().rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    main()

