class Solution(object):
    def beautifulSubsets(self, nums, k):
        nums = sorted(nums)
        count = 0

        def backtrack(idx, subset):
            nonlocal count
            if idx == len(nums):
                if subset:
                    count += 1
                return

            backtrack(idx + 1, subset)

            is_include = True
            for num in subset:
                if abs(num - nums[idx]) == k:
                    is_include = False
                    break

            if is_include:
                backtrack(idx + 1, subset + [nums[idx]])

        backtrack(0, [])

        return count


print(Solution().beautifulSubsets(nums=[2, 4, 6], k=2))
