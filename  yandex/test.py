class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                print(nums)

        return nums


print(Solution().moveZeroes([1, 2, 3, 4, 6]))
