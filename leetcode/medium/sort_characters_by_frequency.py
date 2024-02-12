class Solution(object):
    def frequencySort(self, s):
        history = {}
        result = ''
        for ch in s:
            history[ch] = history.get(ch, 0) + 1

        history = sorted(history.items(), key=lambda x: x[1], reverse=True)
        for h in history:
            result += h[0] * h[1]

        return result


def main():
    print(Solution().frequencySort("tree"))


if __name__ == '__main__':
    main()

