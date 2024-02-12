import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    return check_height(root) != -1


def check_height(node):
    if node is None:
        return 0

    left_height = check_height(node.left)
    right_height = check_height(node.right)

    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
