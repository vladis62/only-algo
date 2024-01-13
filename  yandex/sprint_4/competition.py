def competition(arr):
    hash = {}
    result = 0
    max_sum = 0

    for i in range(len(arr)):
        max_sum += -1 if arr[i] == 0 else 1

        if max_sum == 0:
            result = i + 1

        if max_sum in hash:
            result = max(result, i - hash[max_sum])
        else:
            hash[max_sum] = i
    return result


def main():
    n = int(input())
    if n < 2:
        print(0)
        return
    arr = list(map(int, input().split(' ')))
    print(competition(arr))


if __name__ == '__main__':
    main()
