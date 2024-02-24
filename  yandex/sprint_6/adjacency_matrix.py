def main():
    n, m = map(int, input().split())
    adjacency_matrix = [[0] * n for i in range(n)]

    while m > 0:
        m -= 1
        row, column = list(map(int, input().split()))
        adjacency_matrix[row - 1][column - 1] = 1

    for row in adjacency_matrix:
        print(*row)


if __name__ == '__main__':
    main()
