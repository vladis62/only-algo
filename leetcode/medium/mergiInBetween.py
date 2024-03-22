# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        prev_a = None
        prev_b = None
        node = list1
        index = 0

        while node:
            if index == a - 1:
                prev_a = node
            if index == b:
                prev_b = node
                break
            node = node.next
            index += 1

        prev_a.next = list2
        node = list2

        while node.next:
            node = node.next

        node.next = prev_b.next

        return list1

