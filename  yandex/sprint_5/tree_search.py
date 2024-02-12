import sys

LOCAL = 'true'
sys.setrecursionlimit(2000)

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(nood) -> bool:
    def is_bst(node: Node, min_v, max_v):
        if node is None:
            return True
        if not(min_v < node.value < max_v):
            return False

        return is_bst(node.left, min_v, node.value) and is_bst(node.right, node.value, max_v)

    return is_bst(nood, float('-inf'), float('+inf'))


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
