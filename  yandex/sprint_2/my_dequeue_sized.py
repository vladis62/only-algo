class MyDequeueSized:
    def __init__(self, max_sized):
        self.queue = [None for _ in range(max_sized)]
        self.max_sized = max_sized
        self.head = 0
        self.tail = 0
        self.length = 0

    def push(self, item):
        if self.length != self.max_sized:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_sized
            self.length += 1
        else:
            print('error')

    def peek(self):
        if self.length == 0:
            print(None)
        else:
            print(self.queue[self.head])

    def size(self):
        print(self.length)

    def pop(self):
        if self.length == 0:
            print(None)
            return
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_sized
        self.length -= 1
        print(x)


def main():
    n = int(input())
    size = int(input())
    dequeue = MyDequeueSized(size)
    for i in range(0, n):
        line = input().split()
        if line[0] == 'peek':
            dequeue.peek()
        elif line[0] == 'push':
            dequeue.push(int(line[1]))
        elif line[0] == 'size':
            dequeue.size()
        else:
            dequeue.pop()


if __name__ == '__main__':
    main()

# 13
# 8
# push -82
# push -25
# push -57
# push -24
# size
# push 12
# push 21
# push 62
# push 64
# push -90
# size
# pop
# peek
