class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        history = {}
        for i in range(n):
            if nums[i] in history:
                idx = history[nums[i]]
                if abs(idx - i) <= k:
                    return True
                else:
                    history[nums[i]] = i
            else:
                history[nums[i]] = i

        return False


print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
