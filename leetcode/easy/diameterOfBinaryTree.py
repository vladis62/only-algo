class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        result = 0

        def helper(node):
            nonlocal result
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            result = max(result, left + right)
            return max(left, right) + 1

        helper(root)
        return result


def main():
    n = int(input())
    print(Solution().diameterOfBinaryTree(n))


if __name__ == '__main__':
    main()
