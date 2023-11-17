n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def two_sum():
    left = 0
    right = n - 1

    while left < right:
        if k == arr[left] + arr[right]:
            return str(arr[left]) + " " + str(arr[right])
        if arr[left] + arr[right] > k:
            right -= 1
        else:
            left += 1


print(two_sum())
