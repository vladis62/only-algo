# ID - 109058754

# -- ПРИНЦИП РАБОТЫ --
# Пользуемся двумерным массивом dp, где dp[i][j] представляет собой редакционное расстояние между префиксами строк s1[:j] и s2[:i]
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n * m), n - длина первой строки, m - длина второй строки
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(n * m), n - длина первой строки, m - длина второй строки

def levenshtein(s1, s2):
    n, m = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (0 if s1[j - 1] == s2[i - 1] else 1))

    return dp[m][n]


def main():
    str1, str2 = input(), input()
    print(levenshtein(str1, str2))


if __name__ == '__main__':
    main()


# Второе решение - без использования двумерного массива, сильно экономим по памяти
# ID - 109066421

# -- ПРИНЦИП РАБОТЫ --
# В массиве поиндексно обновляется расстояние редактирования для текущего символа,
# в переменной mem храним значение расстояния редактирования для предыдущего индекса предыдущей строки
# (т.е. обновлённое на предыдущем шаге)
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n * m), n - длина первой строки, m - длина второй строки
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(m), m - длина второй строки

def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [j for j in range(m)]
    for i in range(1, n):
        for j in range(m):
            dist = i if j == 0 else min(dp[j - 1] + 1, dp[j] + 1, mem + int(s1[j] != s2[i]))
            mem = dp[j]
            dp[j] = dist
    return dist


def main():
    str1, str2 = '_' + input(), '_' + input()
    print(levenshtein(str1, str2))


if __name__ == '__main__':
    main()
