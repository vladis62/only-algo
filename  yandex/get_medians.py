from sortedcontainers import SortedList

def get_medians(arr, window_size):
    def get_median(arr):
        if len(arr) % 2 == 1:
            return arr[len(arr) // 2]
        else:
            return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2

    window = SortedList(arr[:window_size])
    result = [get_median(window)]
    for i in range(window_size, len(arr)):
        window.remove(arr[i - window_size])
        window.add(arr[i])
        result.append(get_median(window))
    return result
