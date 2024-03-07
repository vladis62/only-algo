def stair_jump(n, k):
    # module = 1000000007
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, min(k, i) + 1):
            dp[i] += dp[i - j]
            # dp[i] %= module

    return dp[n]


def main():
    n, k = list(map(int, input().split()))
    print(stair_jump(n, k))


if __name__ == '__main__':
    main()
