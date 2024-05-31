class Solution(object):
    def findMaxK(self, nums):
        history = set(nums)
        nums = sorted(nums, reverse=True)

        for num in nums:
            if (-1 * num) in history:
                return num
            if num <= 0:
                break

        return -1


print(Solution().findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
