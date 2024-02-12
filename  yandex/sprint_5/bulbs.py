import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    def search(node):
        nonlocal max_bulb
        if node:
            max_bulb = max(max_bulb, node.value)
            search(node.left)
            search(node.right)

    max_bulb = -999
    search(root)
    return max_bulb


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    print(solution(node4))
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
