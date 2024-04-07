class Solution(object):
    def maxSubarrayLength(self, nums, k):
        i = j = 0
        n = len(nums)
        ans = 1
        map = {}

        while i < n:
            map[nums[i]] = map.get(nums[i], 0) + 1
            while map[nums[i]] > k:
                print(map[nums[j]])
                map[nums[j]] = map[nums[j]] - 1
                j += 1
            ans = max(ans, i - j + 1)
            i += 1
        return ans


print(Solution().maxSubarrayLength([1, 4, 4, 3], 1))
