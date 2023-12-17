# ID - 103185843
# -- ПРИНЦИП РАБОТЫ --
# Я реализовал быструю соритровку без использования дополнительной памяти
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(Nlog(N)) - с помощью pivot разделяем каждый раз массив.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(N). Каждый вызов partition - основной массив делится на подмассив
def quick_sort(arr, l, r):
    def partition(l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    if l < r:
        pivot_idx = partition(l, r)
        quick_sort(arr, l, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, r)


def main():
    n = int(input())
    array = [(-int(task), int(fine), login) for _ in range(n) for login, task, fine in [input().split(' ')]]
    quick_sort(array, 0, len(array) - 1)
    for e in array:
        print(e[2])


if __name__ == '__main__':
    main()
