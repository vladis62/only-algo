class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if A == B and C == D:
            return 1
        if A == C and B == D:
            return 1
        if A == D and C == B:
            return 1
        return 0


print(Solution().solve(1, 2, 2, 2))
