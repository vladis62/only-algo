def perimeter_triangle(sides):
    sides = sorted(sides, reverse=True)
    for i in range(0, len(sides) - 2):
        if sides[i] < sides[i + 1] + sides[i + 2]:
            return sides[i] + sides[i + 1] + sides[i + 2]


def main():
    _ = input()
    sides = list(map(int, input().split(' ')))
    print(perimeter_triangle(sides))


if __name__ == '__main__':
    main()
