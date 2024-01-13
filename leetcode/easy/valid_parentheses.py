class Solution(object):
    def isValid(self, s):
        stack = []
        open_to_closed = {'(': ')', '[': ']', '{': '}'}
        open = {'(', '[', '{'}
        for brace in s:
            if brace in open:
                stack.append(brace)
                continue
            elif not stack:
                return False
            brace_in_stack = stack.pop()
            if brace != open_to_closed[brace_in_stack]:
                return False
        return False if stack else True


def main():
    print(Solution().isValid('((('))


if __name__ == '__main__':
    main()
