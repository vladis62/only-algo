# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        sum_to_count = {0: 1}
        result = 0
        sum = 0

        for num in nums:
            sum += num
            temp = sum - k
            if temp in sum_to_count:
                result += sum_to_count[temp]
            sum_to_count[sum] = sum_to_count.get(sum, 0) + 1

        return result


print(Solution().subarraySum([1, -1, 0], 0))

# 1 1
#   1 1
#     1
