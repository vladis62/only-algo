class Solution(object):
    def lengthOfLastWord(self, s):
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and result != 0:
                break
            elif s[i] == ' ':
                continue
            else:
                result += 1
        return result


print(Solution().lengthOfLastWord("   "))
