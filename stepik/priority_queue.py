class PriorityQueue:
    def __init__(self):
        self.heap = [-1]

    def sift_up(self, idx) -> int:
        while idx > 1:
            next_idx = idx // 2
            if self.heap[idx] > self.heap[next_idx]:
                self.heap[idx], self.heap[next_idx] = self.heap[next_idx], self.heap[idx]
            else:
                break
            idx = next_idx
        return idx

    def head_add(self, e):
        self.heap.append(e)
        idx = len(self.heap) - 1
        self.sift_up(idx)

    def sift_down(self, idx):
        while 2 * idx < len(self.heap):
            left_child_idx = 2 * idx
            right_child_idx = 2 * idx + 1
            max_child_idx = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[left_child_idx]:
                max_child_idx = right_child_idx
            if self.heap[max_child_idx] > self.heap[idx]:
                self.heap[idx], self.heap[max_child_idx] = self.heap[max_child_idx], self.heap[idx]
                idx = max_child_idx
            else:
                break

    def extract_max(self):
        if len(self.heap) == 1:
            return None
        max_item = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.sift_down(1)
        return max_item


def main():
    n = int(input())
    heap = PriorityQueue()

    for i in range(n):
        action = input().split()
        if action[0] == 'Insert':
            heap.head_add(int(action[1]))
        else:
            print(heap.extract_max())


if __name__ == '__main__':
    main()
