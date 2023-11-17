import sys
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'


if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(a, x, b, c):
    return a * x * x + b * x + c


def main():
    line = sys.stdin.readline().rstrip()
    a, x, b, c = line.split()
    a = int(a)
    x = int(x)
    b = int(b)
    c = int(c)
    result = solution(a, x, b, c)
    print(result)


if __name__ == '__main__':
    main()

