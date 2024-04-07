class Solution(object):
    def firstMissingPositive(self, nums):
        positive = set()

        for num in nums:
            if num > 0:
                positive.add(num)

        nums = sorted(positive)
        n = len(positive)
        print(positive)

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


print(Solution().firstMissingPositive([0,2,2,1,1]))
