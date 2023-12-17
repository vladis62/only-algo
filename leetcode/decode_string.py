class Solution(object):
    def decodeString(self, s):
        result = ''
        num = 0
        stack = []
        for e in s:
            if e == '[':
                stack.append(result)
                stack.append(num)
                result = ''
                num = 0
            elif e == ']':
                num = stack.pop()
                pre_str = stack.pop()
                result = pre_str + num * result
                num = 0
            elif e.isdigit():
                num = num * 10 + int(e)
            else:
                result += e

        return result


def main():
    print(Solution().decodeString("3[a2[c]]"))


if __name__ == '__main__':
    main()
