# ID - 107135709

# -- ПРИНЦИП РАБОТЫ --
# Алгоритм состоит из двух частей:
# 1) Добавляем в кучу элемент и при каждом добавлении происходит просеивание по индексу вверх.
# В куче будет храниться первый отсотированный элемент.
# 2) Формируем сортированный список, забирая первый элемент из кучи и просеивание по индексу вниз.
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(n * log(n)), n - количество элементов
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(n) - хранение кучи и конечного отсортированного массива

def heap_sort(heap):
    sorted_array = []
    while len(heap) > 1:
        max_val = pop_max(heap)
        sorted_array.append(max_val[0])

    return sorted_array


def head_add(heap, e):
    heap.append(e)
    idx = len(heap) - 1
    sift_up(heap, idx)


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result


def compare(a, b):
    a_login, a_task, a_fine = a
    b_login, b_task, b_fine = b
    if a_task < b_task:
        return -1
    if a_task > b_task:
        return 1

    if a_task == b_task:
        if a_fine < b_fine:
            return 1
        if a_fine > b_fine:
            return -1

        if a_fine == b_fine:
            if a_login < b_login:
                return 1
            if a_login > b_login:
                return -1


def sift_down(heap, idx) -> int:
    n = len(heap) - 1
    left = 2 * idx
    right = 2 * idx + 1
    while n >= left:
        if right <= n and compare(heap[left], heap[right]) == -1:
            idx_largest = right
        else:
            idx_largest = left
        if compare(heap[idx], heap[idx_largest]) == -1:
            heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
            idx = idx_largest
        left = 2 * idx_largest
        right = 2 * idx_largest + 1
    return idx


def sift_up(heap, idx) -> int:
    while idx > 1:
        parent_idx = idx // 2
        if compare(heap[idx], heap[parent_idx]) == 1:
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
            idx = parent_idx
        else:
            break
    return idx


def main():
    n = int(input())
    heap = [-1]

    for i in range(n):
        login, task, fine = input().split()
        head_add(heap, [login, int(task), int(fine)])
    sorted_array = heap_sort(heap)
    [print(arr) for arr in sorted_array]


if __name__ == '__main__':
    main()
