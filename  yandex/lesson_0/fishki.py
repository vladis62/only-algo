n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def two_sum(n, arr, k):
    num_to_index = {}
    for i in range(n):
        if k - arr[i] in num_to_index:
            return str(arr[num_to_index[k - arr[i]]]) + " " + str(arr[i])
        num_to_index[arr[i]] = i
    return None


print(two_sum(n, arr, k))

