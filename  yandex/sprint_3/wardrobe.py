def wardrobe(arr, k):
    result = [0] * k
    for e in arr:
        result[e] += 1

    index = 0
    for value in range(k):
        for amount in range(result[value]):
            arr[index] = value
            index += 1


def main():
    n = int(input())
    if n < 1:
        print('')
        return
    arr = list(map(int, input().split(' ')))
    wardrobe(arr, 3)
    print(*arr)


if __name__ == '__main__':
    main()
