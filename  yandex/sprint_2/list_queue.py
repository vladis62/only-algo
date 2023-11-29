class ListQueue:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def put(self, x):
        node = self.Node(x)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def size(self):
        print(self.length)

    def get(self):
        if self.length == 0:
            print('error')
        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            print(value)


def main():
    n = int(input())
    queue = ListQueue()
    for i in range(0, n):
        line = input().split()
        if line[0] == 'get':
            queue.get()
        elif line[0] == 'put':
            queue.put(int(line[1]))
        else:
            queue.size()


if __name__ == '__main__':
    main()
