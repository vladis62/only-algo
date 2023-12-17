def diff_indexes(arr, k):
    arr.sort()
    l, r = 0, arr[-1] - arr[0]
    while l < r:
        mid = (l + r) // 2
        if get_diff(mid, arr) >= k:
            r = mid
        else:
            l = mid + 1
    return l


def get_diff(mid, arr):
    l = 0
    diff = 0
    for r in range(len(arr)):
        while arr[r] - arr[l] > mid:
            l += 1
        diff += r - l
    return diff


def main():
    _ = int(input())
    arr = list(map(int, input().split(' ')))
    k = int(input())
    print(diff_indexes(arr, k))


if __name__ == '__main__':
    main()
