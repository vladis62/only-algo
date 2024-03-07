class Heap:
    def __init__(self, m):
        self.weight = 0
        self.capacity = [0] * (m + 1)


def max_profit_golds(weights, m):
    previous = Heap(m)

    gold_heap = Heap(m)
    for weight in weights:
        gold_heap = Heap(m)
        for g in range(m + 1):
            if g - weight >= 0:
                gold_heap.capacity[g] = max(previous.capacity[g], weight + previous.capacity[g - weight])
            else:
                gold_heap.capacity[g] = previous.capacity[g]
        previous = gold_heap

    return gold_heap.capacity[m]


def main():
    n, m = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(max_profit_golds(weights, m))


if __name__ == '__main__':
    main()
