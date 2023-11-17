class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            left += 1
            right -= 1
            if s[left] != s[right]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(11))
