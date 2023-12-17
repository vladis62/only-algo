def buy_houses(houses, sum):
    houses = sorted(houses)
    count = 0
    for house in houses:
        if sum - house >= 0:
            sum -= house
            count += 1
        else:
            return count
    return count


def main():
    _, sum = list(map(int, input().split(' ')))
    houses = list(map(int, input().split(' ')))
    print(buy_houses(houses, sum))


if __name__ == '__main__':
    main()
