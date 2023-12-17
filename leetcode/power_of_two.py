class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 2 or n == 1:
            return True
        if n % 2 != 0 or n == 0:
            return False
        return self.isPowerOfTwo(n // 2)


print(Solution().isPowerOfTwo(60))
