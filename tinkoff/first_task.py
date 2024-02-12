import math


def first_task(x, y):
    coordinate = math.sqrt(pow(x, 2) + pow(y, 2))
    if coordinate <= 0.1:
        return 3
    if 0.1 < coordinate <= 0.8:
        return 2
    if 0.8 < coordinate <= 1:
        return 1
    return 0


def main():
    result = 0
    for _ in range(3):
        line = list(map(float, input().split()))
        x = line[0]
        y = line[1]
        result += first_task(x, y)

    print(result)


if __name__ == '__main__':
    main()
