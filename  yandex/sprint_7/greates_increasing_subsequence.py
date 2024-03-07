def greatest_increasing_subsequence(seq, n):
    dp = [1] * n
    max_value = 1

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_value = max(max_value, dp[i])

    ans = []
    for i in range(n - 1, -1, -1):
        if dp[i] == max_value:
            max_value -= 1
            ans.append(i + 1)

    return [len(ans), ans[::-1]]


def main():
    n = int(input())
    seq = list(map(int, input().split()))

    length, ans = greatest_increasing_subsequence(seq, n)

    print(length)
    print(*ans)


if __name__ == '__main__':
    main()
