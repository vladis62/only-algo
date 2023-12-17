class Solution(object):
    def __init__(self):
        self.nums = set()

    def isHappy(self, n):
        if n == 1:
            return True
        num = 0
        for m in str(n):
            num += pow(int(m), 2)
        if num in self.nums:
            return False
        self.nums.add(num)
        return self.isHappy(num)


print(Solution().isHappy(2))
