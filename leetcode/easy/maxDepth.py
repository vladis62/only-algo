# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution(object):
    def maxDepth(self, s):
        stack = []
        sizes = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                sizes.append(len(stack))
                stack.pop()

        if not sizes:
            return 0
        return max(sizes)


print(Solution().maxDepth("(1)+((2))+(((3)))"))

