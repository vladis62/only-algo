class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def smallestFromLeaf(self, root):
        smallest_str = '~'

        def dfs(node, path):
            nonlocal smallest_str
            if node:
                path += chr(node.val + ord('a'))

                if not node.left and not node.right:
                    temp_str = path[::-1]
                    if temp_str < path:
                        smallest_str = temp_str
                else:
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, '')
        return smallest_str
