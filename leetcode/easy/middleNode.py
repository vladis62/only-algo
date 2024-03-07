# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def middleNode(self, head):
#         node = head
#         size = 0
#
#         while node:
#             size += 1
#             node = node.next
#
#         node = head
#         size //= 2
#         while size > 0:
#             node = node.next
#             size -= 1
#         return node
class Solution(object):
    def middleNode(self, head):
        slow = fast = head

        while fast:
            slow = head.next
            fast = slow.next

        return slow


