import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item
    previous_node = get_node_by_index(node, idx - 1)
    if previous_node.next_item.next_item is None:
        previous_node.next_item = None
    else:
        previous_node.next_item = previous_node.next_item.next_item
    return node


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 2)
    next_node = new_head
    while next_node is not None:
        print(next_node.value)
        next_node = next_node.next_item
    assert new_head is node0
    assert new_head.next_item is node1
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


def test1():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 0)
    assert new_head is node1
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


if __name__ == '__main__':
    test1()
