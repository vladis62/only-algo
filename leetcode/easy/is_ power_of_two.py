class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n < 1 or n % 2 == 1:
            return False
        return self.isPowerOfTwo(n >> 1)


def main():
    print(Solution().isPowerOfTwo(3))


if __name__ == '__main__':
    main()
