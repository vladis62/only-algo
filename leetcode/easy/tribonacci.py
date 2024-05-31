class Solution:
    def tribonacci(self, n):
        tribonaccies = [0, 1, 1]
        i = 0

        while len(tribonaccies) <= n:
            tribonaccies.append(tribonaccies[i] + tribonaccies[i + 1] + tribonaccies[i + 2])
            i += 1

        return tribonaccies[n]


print(Solution().tribonacci(25))
