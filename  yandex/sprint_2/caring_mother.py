import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, elem):
    next_node = node
    idx = 0
    while next_node is not None:
        if next_node.value == elem:
            return idx
        idx += 1
        next_node = next_node.next_item
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node21")
    assert idx == -1


if __name__ == '__main__':
    test()
