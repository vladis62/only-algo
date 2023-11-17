import sys


def solution(matrix, x, y, n, m):
    neighbours = list()
    if x - 1 >= 0:
        neighbours.append(matrix[x - 1][y])
    if x + 1 <= n - 1:
        neighbours.append(matrix[x + 1][y])
    if y - 1 >= 0:
        neighbours.append(matrix[x][y - 1])
    if y + 1 <= m - 1:
        neighbours.append(matrix[x][y + 1])
    neighbours.sort()
    return ' '.join(str(neighbour) for neighbour in neighbours)


def main():
    n = int(input())
    m = int(input())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(0, n):
        line = sys.stdin.readline().rstrip()
        line = line.split()
        for j in range(0, m):
            matrix[i][j] = int(line[j])
    x = int(input())
    y = int(input())
    result = solution(matrix, x, y, n, m)
    print(result)


if __name__ == '__main__':
    main()

