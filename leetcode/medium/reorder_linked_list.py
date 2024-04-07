class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorder_list(self, head):
        temp = []
        node = head
        while node:
            temp.append(node)
            node = node.next

        n = len(temp)
        if n <= 2:
            return head

        left = 0
        right = n - 1

        while left < right:
            temp[left].next = temp[right]
            left += 1
            if left == right:
                break
            temp[right].next = temp[left]
            right -= 1

        temp[left].next = None

        return head


def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print_list(Solution().reorder_list(head))
