from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def search_node(DNode, DParent, key):
    while DNode and DNode.value != key:
        DParent = DNode
        if key >= DNode.value:
            DNode = DNode.right
        else:
            DNode = DNode.left
    return DNode, DParent


def find_replace_right_node(node, parent_node):
    while node.right:
        parent_node = node
        node = node.right

    return [node, parent_node]


def remove(root, key) -> Optional[Node]:
    node, parent_node = search_node(root, None, key)

    if not node:
        return root

    if not node.left and not node.right:
        if node == root:
            return None
        else:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None

        return root

    if node.left and node.right:
        PParent = node
        PNode, PParent = find_replace_right_node(node.left, PParent)
        node.value = PNode.value
        if PParent.left == PNode:
            PParent.left = PNode.left
        else:
            PParent.right = PNode.left
    else:
        if node.left:
            PNode = node.left
        else:
            PNode = node.right
        if node != root:
            if node == parent_node.left:
                parent_node.left = PNode
            else:
                parent_node.right = PNode
        else:
            node = PNode

    return node


def remove(node, key):
    DNode = node
    DParent = None

    DNode1, DParent = search_node(DNode, DParent, key)

    if not DNode:
        return node

    if not DNode.left and not DNode.right:
        if DNode == node:
            return None
        else:
            if DParent.left == DNode:
                DParent.left = None
            else:
                DParent.right = None
        return node

    if DNode.left and DNode.right:
        PParent = DNode
        PNode, PParent = find_replace_right_node(DNode.left, PParent)
        DNode.value = PNode.value
        if PParent.left == PNode:
            PParent.left = PNode.left
        else:
            PParent.right = PNode.left
    else:
        if DNode.left:
            PNode = DNode.left
        else:
            PNode = DNode.right
        if DNode != node:
            if DNode == DParent.left:
                DParent.left = PNode
            else:
                DParent.right = PNode
        else:
            node = PNode

    return node


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
