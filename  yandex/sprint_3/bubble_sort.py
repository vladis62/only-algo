def bubble_sort(arr, n):
    is_was_swap = True
    for _ in range(n - 1):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_was_swap = True
        if is_was_swap:
            print(*arr)
            is_was_swap = False


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr, n)


if __name__ == '__main__':
    main()
