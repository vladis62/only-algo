class Solution(object):
    def makeGood(self, s):
        n = len(s)
        i = 0

        while i < (n - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                s = s[0:i] + s[i+2:n]
                n = len(s)
                if i > 0:
                    i -= 1
            else:
                i += 1

        return s


print(Solution().makeGood("abBAcC"))
