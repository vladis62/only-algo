class Node:
    def __init__(self, value):
        self.value = value
        self.to = []


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = size - 1

    def push(self, value):
        self.stack[self.top] = value
        self.top -= 1

    def __str__(self):
        return ' '.join(str(val) for val in self.stack[self.top + 1:])


def topological_sort(peaks, nodes):
    colors = [''] * (peaks + 1)
    stack = Stack(peaks)

    def sort(node):
        colors[node.value] = "gray"
        for next_node in node.to:
            if colors[next_node.value] == "":
                sort(next_node)
        colors[node.value] = "black"
        stack.push(node.value)

    for i in range(peaks, 0, -1):
        if colors[i] == "":
            sort(nodes[i])

    return stack


def main():
    peaks, edges = map(int, input().split())

    nodes = [Node(i) for i in range(peaks + 1)]

    for _ in range(edges):
        peak_a, peak_b = map(int, input().split())
        nodes[peak_a].to.append(nodes[peak_b])

    print(topological_sort(peaks, nodes))


if __name__ == '__main__':
    main()
