class Solution(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        current = head
        result = None
        while current:
            new_node = current.next
            current.next = result
            result = current
            current = new_node
        return result


def main():
    print(Solution().reverseList([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
