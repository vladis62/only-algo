class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


def main():
    print(Solution().longestCommonSubsequence("abcde", "ace"))


if __name__ == '__main__':
    main()
