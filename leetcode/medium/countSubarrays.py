class Solution:
    def countSubarrays(self, nums, k):
        max_num = max(nums)
        result, l, r = 0, 0, 0
        n = len(nums)

        while r < n:
            if nums[r] == max_num:
                k -= 1
            r += 1

            while k == 0:
                if nums[l] == max_num:
                    k += 1
                l += 1
            result += l

        return result


print(Solution().countSubarrays(
    [61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58, 42, 82, 10, 82, 78, 15, 82], 2))
