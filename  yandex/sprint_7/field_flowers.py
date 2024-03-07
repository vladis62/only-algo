def field_flowers(field, n, m):
    dp = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    data = [[-1 for _ in range(m + 1)]]
    for row in field:
        data.append([-1] + row + [-1])
    data.append([-1 for _ in range(m + 1)])

    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + data[i][j]

    return dp[1][m]


def main():
    n, m = list(map(int, input().split()))
    field = [[int(digit) for digit in input()] for _ in range(n)]
    print(field_flowers(field, n, m))


if __name__ == '__main__':
    main()
