class Solution(object):
    def divide_array(self, nums, k):
        n = len(nums)
        result = []
        nums.sort()

        for i in range(0, n - 2, 3):
            if nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return result


nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2
result = Solution().divide_array(nums, k)
print(result)
