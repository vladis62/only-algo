# ID - 109058754

# -- ПРИНЦИП РАБОТЫ --
# Считаем сумму очков, в dp пишем True, если сумма j может быть достигнута
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n * m), n - элементы массива, m - сумма очков
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(m), m - половина суммы всех элементов n массива

def is_equal_amounts(scores):
    sum_scores = sum(scores)
    if sum_scores % 2 != 0:
        return False

    half_sum = sum_scores // 2
    dp = [False] * (half_sum + 1)
    dp[0] = True
    for point in scores:
        for j in range(half_sum, point - 1, -1):
            dp[j] = dp[j - point] or dp[j]
            if j == half_sum and dp[j]:
                return True
    return dp[half_sum]


def main():
    _ = int(input())
    points = list(map(int, input().split()))
    print(is_equal_amounts(points))


if __name__ == '__main__':
    main()

