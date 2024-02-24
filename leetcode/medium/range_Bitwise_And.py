class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


def main():
    print(Solution().rangeBitwiseAnd(1, 12))


if __name__ == '__main__':
    main()


