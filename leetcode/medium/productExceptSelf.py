from functools import reduce


class Solution(object):
    def productExceptSelf(self, nums):
        mult = reduce(lambda x, y: x * y, nums)
        result = []

        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(mult // nums[i])
            else:
                result.append(multiply_array_elements(nums, i))

        return result


def multiply_array_elements(nums, ex_i):
    result = 1
    for i in range(len(nums)):
        if i != ex_i:
            result *= nums[i]
    return result


print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
