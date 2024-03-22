class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length = 0
        history = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in history:
                max_length = max(max_length, i - history[count])
            else:
                history[count] = i

        return max_length


print(Solution().findMaxLength([0, 1]))
