class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


def main():
    n = int(input())
    stack_max = StackMax()
    for i in range(0, n):
        line = input().split()
        if line[0] == 'get_max':
            print(stack_max.get_max())
        elif line[0] == 'push':
            stack_max.push(int(line[1]))
        else:
            size = stack_max.pop()
            if size is None:
                print('error')


if __name__ == '__main__':
    main()
