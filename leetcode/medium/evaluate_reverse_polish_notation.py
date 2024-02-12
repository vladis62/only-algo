# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=daily-question&envId=2024-01-30
import math


class Solution(object):
    def evalRPN(self, tokens):
        expression = {'-', '+', '/', '*'}
        stack = []
        for token in tokens:
            if token in expression:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '-':
                    result = operand2 - operand1
                elif token == '/':
                    result = int(float(operand2 / operand1))
                elif token == '*':
                    result = operand2 * operand1
                else:
                    result = operand2 + operand1
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


def main():
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    # print(6 // -132)


if __name__ == '__main__':
    main()
