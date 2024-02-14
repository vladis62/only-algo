# ID - 107195101

# -- ПРИНЦИП РАБОТЫ --
#  Ищем удаляемый элемент, если элемент не найден - возвращаем root
#  Если у найденного элемента нет детей, то у родительского элемента присваиваем None (удаляем).
#  Если найденный элемент является корнем дерева возвращаем None.
#  Если у найденного элемента один ребенок то у родителя меняем элемент на ребенка.
#  Если у найденного элемента двое детей, то ищем в левом ребенке самый правый узел и заменяем его на удаляемый элемент.
#  Меняем значение удаляемого элемента на элемент найденного узла и присваиваем левую часть найденного правого узла.
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(h), h — высота дерева.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# O(n), n - количество элементов.

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


def search_node(node, parent_node, key):
    while node and node.value != key:
        parent_node = node
        node = node.right if key >= node.value else node.left
    return node, parent_node


def find_replace_right_node(node, parent_node):
    while node.right:
        parent_node = node
        node = node.right

    return [node, parent_node]


def remove(root, key) -> Optional[Node]:
    node, parent_node = search_node(root, Node, key)

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
        p_parent_node = node
        p_node, p_parent_node = find_replace_right_node(node.left, p_parent_node)
        node.value = p_node.value
        if p_parent_node.left == p_node:
            p_parent_node.left = p_node.left
        else:
            p_parent_node.right = p_node.left
    else:
        p_node = node.left if node.left else node.right
        if node != root:
            if node == parent_node.left:
                parent_node.left = p_node
            else:
                parent_node.right = p_node
        else:
            root = p_node

    return root


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
