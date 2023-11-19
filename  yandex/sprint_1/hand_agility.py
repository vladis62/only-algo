def hand_agility(matrix, n):
    max_touch = n * 2
    numbers_to_count = {}
    for i in range(0, 4):
        for j in range(0, 4):
            num = matrix[i][j]
            if matrix[i][j] != '.':
                numbers_to_count[num] = numbers_to_count.get(num, 0) + 1
    points = 0
    for _, count in numbers_to_count.items():
        if count <= max_touch:
            points = points + 1
    return points


def main():
    n = int(input())
    matrix = [['' for _ in range(4)] for _ in range(4)]
    for i in range(0, 4):
        line = input().replace('', ' ').split()
        for j in range(0, 4):
            matrix[i][j] = line[j]
    print(hand_agility(matrix, n))


if __name__ == '__main__':
    main()
