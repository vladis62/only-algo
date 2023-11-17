n = int(input())
arr = list(map(int, input().split()))
k = int(input())
slice_window = []
sum = 0

for i in range(0, k):
    sum += arr[i]
slice_window.append(sum / k)

for i in range(0, n - k):
    sum -= arr[i]
    sum += arr[i + k]
    slice_window.append(sum / k)

print(" ".join(list(map(str, slice_window))))
