def longest_common_subsequence(seq1, seq2, n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    ans1, ans2 = [], []
    i, j = n, m

    while dp[i][j] != 0:
        if dp[i - 1][j] == dp[i][j - 1]:
            if seq1[i - 1] == seq2[j - 1]:
                ans1.append(i)
                ans2.append(j)
                i -= 1
                j -= 1
            else:
                i -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return [dp[n][m], ans1[::-1], ans2[::-1]]


def main():
    n = int(input())
    seq1 = list(map(int, input().split()))
    m = int(input())
    seq2 = list(map(int, input().split()))

    length, ans1, ans2 = longest_common_subsequence(seq1, seq2, n, m)

    print(length)
    print(*ans1)
    print(*ans2)


if __name__ == '__main__':
    main()
