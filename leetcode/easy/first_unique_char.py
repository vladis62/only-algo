class Solution:
    def firstUniqChar(self, s: str) -> int:
        history = {}
        for i, ch in enumerate(s):
            if ch in history:
                arr = history[ch]
                history[ch] = [arr[0], arr[1] + 1]
            else:
                history[ch] = [i, 1]

        # index and value
        min_i = [-1, 0]
        for _, e in history.items():
            if e[1] == 1:
                if e[0] < min_i[0] or min_i[0] == -1:
                    min_i = e

        return min_i[0]

def main():
    print(Solution().firstUniqChar("leetcode"))


if __name__ == '__main__':
    main()
