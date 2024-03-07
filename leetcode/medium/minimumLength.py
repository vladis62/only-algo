class Solution(object):
    def minimumLength(self, s):
        n = len(s)
        l, r = 0, n - 1

        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while l <= r and s[r] == ch:
                r -= 1
        return abs(l - r - 1)


def main():
    print(Solution().minimumLength("ca"))


if __name__ == '__main__':
    main()
