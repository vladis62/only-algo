def sift_up(heap, idx) -> int:
    while idx > 1:
        next_idx = idx // 2
        if heap[idx] > heap[next_idx]:
            heap[idx], heap[next_idx] = heap[next_idx], heap[idx]
        else:
            break
        idx = next_idx
    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
