# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        result = float('inf')
        prev = float('inf')

        def in_order(node):
            nonlocal result
            nonlocal prev
            if node.left:
                in_order(node.left)

            result = min(result, abs(node.val - prev))
            prev = node.val

            if node.right:
                in_order(node.right)

        in_order(root)
        return result
