# ID посылки - 98108832


def hand_agility(field, n):
    max_touch = n * 2
    numbers_to_count = {}
    for i in range(0, 4):
        for j in range(0, 4):
            num = field[i][j]
            if field[i][j] != '.':
                numbers_to_count[num] = numbers_to_count.get(num, 0) + 1
    return sum(count <= max_touch for count in numbers_to_count.values())


def main():
    n = int(input())
    field = [input() for _ in range(4)]
    print(hand_agility(field, n))


if __name__ == '__main__':
    main()
