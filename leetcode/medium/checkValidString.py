class Solution(object):
    def checkValidString(self, s):
        leftMin = leftMax = 0

        for ch in s:
            if ch == '(':
                leftMin += 1
                leftMax += 1
            elif ch == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0


print(Solution().checkValidString('()'))
