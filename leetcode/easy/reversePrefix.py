class Solution(object):
    def reversePrefix(self, word, ch):
        n = len(word)
        i = 0
        while i < n:
            if word[i] == ch:
                break
            i += 1
        if i < n:
            return word[:i + 1][::-1] + word[i + 1:]
        return word
