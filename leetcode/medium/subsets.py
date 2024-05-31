class Solution(object):
    def subsets(self, nums):
        def f(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                f(i + 1, path)
                path.pop()

        result = []
        f(0, [])
        return result


print(Solution().subsets(nums=[1, 2, 3]))
