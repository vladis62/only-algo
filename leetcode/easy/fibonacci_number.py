class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)


print(Solution().fib(2))
