class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        if len(num) <= k:
            return "0"

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        return str(int(''.join(stack)))


print(Solution().removeKdigits(num="1432219", k=3))
