class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(f'{n:032b}'[::-1], 2)


print(Solution().reverseBits(int('00000010100101000001111010011100', 2)))
