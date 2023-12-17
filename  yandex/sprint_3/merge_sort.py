def merge(arr, lf, mid, rg):
    n1, n2 = mid - lf, rg - mid

    left, right = [0] * n1, [0] * n2

    for i in range(0, n1):
        left[i] = arr[lf + i]

    for j in range(0, n2):
        right[j] = arr[mid + j]

    i, j, k = 0, 0, lf
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr, lf, rg):
    if rg - lf > 1:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
