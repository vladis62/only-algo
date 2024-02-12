class Solution(object):
    def groupAnagrams(self, strs):
        result = {}
        if not strs:
            return []
        if len(strs) == 1:
            return [[strs[0]]]
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in result:
                arr = result[s_sorted]
                arr.append(s)
                result[s_sorted] = arr
            else:
                result[s_sorted] = [s]
        return list(result.values())


def main():
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()
