# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths(self, root):
        def is_pseudo_palindrome(freq):
            odd_count = 0
            for count in freq.values():
                if count % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, freq):
            if not node:
                return 0

            freq[node.val] += 1

            if not node.left and not node.right:
                result = 1 if is_pseudo_palindrome(freq) else 0
            else:
                result = dfs(node.left, freq) + dfs(node.right, freq)

            freq[node.val] -= 1

            return result

        return dfs(root, {i: 0 for i in range(1, 10)})

