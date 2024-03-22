class Solution(object):
    def pivotInteger(self, n):
        sum = (n * (n + 1)) // 2
        sum1 = sum
        sum2 = 0

        while n > 0:
            sum2 += n
            if sum1 == sum2:
                return n
            sum1 -= n
            n -= 1
        return -1


print(Solution().pivotInteger(8))

