class Solution(object):
    def isPalindrome(self, head):
        arr = []
        node = head

        while node:
            arr.append(node.val)
            node = node.next

        left, right = 0, len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True
