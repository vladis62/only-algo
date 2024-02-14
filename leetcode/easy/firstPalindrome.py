class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""


def main():
    print(Solution().firstPalindrome(["notapalindrome", "racecar"]))


if __name__ == '__main__':
    main()
