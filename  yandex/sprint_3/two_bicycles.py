def two_bicycles(arr, e, left, right):
    if left >= right != 0:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= e > arr[mid - 1] or mid == 0:
        return mid + 1
    if arr[mid] >= e:
        return two_bicycles(arr, e, left, mid)
    else:
        return two_bicycles(arr, e, mid + 1, right)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    e = int(input())
    a = two_bicycles(arr, e, 0, n)
    b = two_bicycles(arr, e * 2, 0, n)
    print(f'{a} {b}')


if __name__ == '__main__':
    main()
