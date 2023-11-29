def solution(matrix, n, m):
    return [[matrix[j][i] for j in range(n)] for i in range(m)]


def main():
    n = int(input())
    m = int(input())
    matrix = [input().split() for _ in range(n)]
    result = solution(matrix, n, m)
    for i in range(m):
        print(*result[i])


if __name__ == '__main__':
    main()
