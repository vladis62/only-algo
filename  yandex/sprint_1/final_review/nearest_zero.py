# ID посылки - 98103991


def nearest_zero(houses):
    result = list()
    count = 1
    for i in range(0, len(houses)):
        if houses[i] == 0:
            handle_pick_period(result, count, i - 1)
            result.append(houses[i])
            count = 1
        else:
            result.append(count)
            count += 1
    return result


def handle_pick_period(result, length, end):
    if length == 1:
        return
    count = 1
    if len(result) == length - 1:
        middle = -1
    else:
        middle = end - length // 2
    for i in range(end, middle, -1):
        result[i] = count
        count += 1


def main():
    _ = input()
    arr = list(map(int, input().split()))
    result = nearest_zero(arr)
    print(*result)


if __name__ == '__main__':
    main()
