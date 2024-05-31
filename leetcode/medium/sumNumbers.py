# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def f(node, cur_sum=0):
            if not node:
                return 0

            cur_sum = node.val + 10 * cur_sum

            if not node.right and not node.left:
                return cur_sum

            return f(node.left, cur_sum) + f(node.right, cur_sum)

        return f(root)
