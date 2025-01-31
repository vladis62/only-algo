class Solution(object):
    def findDuplicate(self, nums):
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


print(Solution().findDuplicate([3, 1, 3, 4, 2]))
