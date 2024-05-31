class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left(node, is_left=True):
            if not node:
                return 0
            if not node.left and not node.right and is_left:
                return node.val
            else:
                return sum_left(node.left) + sum_left(node.right, False)

        return sum_left(root)
