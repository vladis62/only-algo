class Solution(object):
    def maximumOddBinaryNumber(self, s):
        countOne = len(list(filter(lambda num: num == '1', s))) - 1
        countZero = len(s) - countOne - 1
        return "1" * countOne + str("0" * countZero) + "1"


def main():
    print(Solution().maximumOddBinaryNumber("10"))


if __name__ == '__main__':
    main()
