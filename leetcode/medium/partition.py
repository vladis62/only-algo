class Solution(object):
    def partition(self, s):
        def combinations(start, path):
            if start == len(s):
                combination.append(path)
                return

            for end in range(start + 1, len(s) + 1):
                combinations(end, path + [s[start:end]])

        def all(arr):
            for e in arr:
                if e != e[::-1]:
                    return False
            return True
        combination = []
        combinations(0, [])
        result = []
        for combo in combination:
            if all(combo):
                result.append(combo)

        return result


print(Solution().partition("aab"))


