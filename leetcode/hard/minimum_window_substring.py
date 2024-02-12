# https://leetcode.com/problems/minimum-window-substring/solutions/4674237/easy-explanation-solution/?envType=daily-question&envId=2024-02-04

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetFreq = {}
        windowFreq = {}

        for char in t:
            targetFreq[char] = targetFreq.get(char, 0) + 1

        left = 0
        right = 0
        minLength = float('inf')
        minLeft = 0
        requiredChars = len(targetFreq)

        while right < len(s):
            currentChar = s[right]
            windowFreq[currentChar] = windowFreq.get(currentChar, 0) + 1

            if currentChar in targetFreq and windowFreq[currentChar] == targetFreq[currentChar]:
                requiredChars -= 1

            while requiredChars == 0:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minLeft = left

                leftChar = s[left]
                windowFreq[leftChar] -= 1

                if leftChar in targetFreq and windowFreq[leftChar] < targetFreq[leftChar]:
                    requiredChars += 1

                left += 1

            right += 1

        if minLength == float('inf'):
            return ""

        return s[minLeft:minLeft + minLength]
