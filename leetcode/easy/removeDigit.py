class Solution(object):
    def removeDigit(self, number, digit):
        result = []

        for i in range(len(number)):
            if number[i] == digit:
                result.append(str(int(number[0:i] + number[i + 1:])))

        return max(result)


print(Solution().removeDigit(number="1231", digit="1"))
