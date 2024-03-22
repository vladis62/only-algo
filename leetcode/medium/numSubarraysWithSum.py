class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        cnt = 0
        prefix_sum = 0
        sum_count = {0: 1}

        for num in nums:
            prefix_sum += num
            cnt += sum_count.get(prefix_sum - goal, 0)
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

        return cnt


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
