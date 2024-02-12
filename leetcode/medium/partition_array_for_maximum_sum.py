# https://leetcode.com/problems/partition-array-for-maximum-sum/?envType=daily-question&envId=2024-02-03

class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        K = k + 1

        dp = [0] * K

        for start in range(n - 1, -1, -1):
            curr_max = 0
            end = min(n, start + k)
            print(start, end)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + curr_max * (i - start + 1))

        print(dp)

        return dp[0]


def main():
    print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 3))


if __name__ == '__main__':
    main()
