def circle(circles):
    result = {}
    for circle in circles:
        if circle not in result:
            print(circle)
            result[circle] = 0


def main():
    n = int(input())
    circles = [input() for _ in range(n)]
    circle(circles)


if __name__ == '__main__':
    main()
