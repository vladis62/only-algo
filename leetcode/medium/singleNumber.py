from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        history = defaultdict(int)
        result = []
        for num in nums:
            history[num] += 1

        for k,v in history.items():
            if v == 1:
                result.append(k)
            if len(result) == 2:
                return result

        return result


print(Solution().singleNumber([-1, 0, 2, 2]))
