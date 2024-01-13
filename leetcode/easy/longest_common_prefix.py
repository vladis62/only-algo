class Solution(object):
    def longest_common_prefix(self, strs):
        max_prefix = strs[0]
        for s in strs:
            for j in range(len(max_prefix)):
                if j >= len(s) or max_prefix[j] != s[j]:
                    max_prefix = max_prefix[:j]
                    list()
                    break

        return max_prefix


def main():
    print(Solution().longest_common_prefix(["flower", "flow", "flight"]))


if __name__ == '__main__':
    main()
