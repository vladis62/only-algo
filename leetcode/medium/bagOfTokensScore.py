class Solution:
    def bagOfTokensScore(self, tokens, power):
        n = len(tokens)

        tokens.sort()
        i, j = 0, n - 1
        score = 0
        res = 0
        while i <= j:
            if power >= tokens[i]:
                score += 1
                res = max(res, score)
                power -= tokens[i]
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                i += 1
        return res



tokens = [200, 100]
power = 150
result = Solution().bagOfTokensScore(tokens, power)
print(result)
