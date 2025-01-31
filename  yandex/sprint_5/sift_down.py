def sift_down(heap, idx) -> int:
    n = len(heap) - 1
    left = 2 * idx
    right = 2 * idx + 1
    while n >= left:
        if right <= n and heap[left] < heap[right]:
            idx_largest = right
        else:
            idx_largest = left
        if heap[idx] < heap[idx_largest]:
            heap[idx], heap[idx_largest] = heap[idx_largest], heap[idx]
            idx = idx_largest
        left = 2 * idx_largest
        right = 2 * idx_largest + 1
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
