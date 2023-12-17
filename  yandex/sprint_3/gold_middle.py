def gold_middle(arr1, arr2):
    arr = sorted(arr1 + arr2)
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


def main():
    _ = input()
    _ = input()
    arr1 = list(map(int, input().split(' ')))
    arr2 = list(map(int, input().split(' ')))
    print(gold_middle(arr1, arr2))


if __name__ == '__main__':
    main()
