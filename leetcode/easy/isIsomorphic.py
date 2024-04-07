class Solution(object):
    def isIsomorphic(self, s, t):
        alphabet_s = {}
        alphabet_t = {}

        for i in range(len(s)):
            ch1 = alphabet_s.get(s[i], t[i])
            ch2 = alphabet_t.get(t[i], s[i])
            if ch1 != t[i] or ch2 != s[i]:
                return False
            else:
                alphabet_s[s[i]] = t[i]
                alphabet_t[t[i]] = s[i]
        return True


print(Solution().isIsomorphic("foo", "title"))
