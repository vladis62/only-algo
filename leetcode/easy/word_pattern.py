class Solution(object):
    def wordPattern(self, pattern, s):
        history = {}
        list_s = s.split()
        n = len(pattern)
        if n != len(list_s):
            return False
        if len(set(pattern)) != len(set(list_s)):
            return False
        for i in range(n):
            if pattern[i] in history:
                word = history[pattern[i]]
                if word != list_s[i]:
                    return False
            else:
                history[pattern[i]] = list_s[i]

        return True


print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
print(Solution().wordPattern(pattern="abba", s="dog dog dog dog"))
