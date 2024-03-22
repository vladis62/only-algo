class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = [num1, num2] if len(num1) >= len(num2) else [num2, num1]
        num2, result, modulo = '0' * (len(num1) - len(num2)) + num2, '', 0

        for i in range(len(num1) - 1, -1, -1):
            sum_num = int(num1[i]) + int(num2[i]) + modulo
            modulo = 1 if sum_num > 9 else 0
            result = str(sum_num % 10) + result

        result = (str(modulo) if modulo == 1 else '') + result

        return result


print(Solution().addStrings("11", "123"))
