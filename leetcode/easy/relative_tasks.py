class Solution(object):
    def findRelativeRanks(self, score):
        sort_score = sorted(score, reverse=True)
        print(score)
        print(sort_score)
        n = len(score)
        result = [''] * n
        for i in range(n):
            for j in range(n):
                if score[i] == sort_score[j]:
                    if j == 0:
                        result[i] = 'Gold Medal'
                    elif j == 1:
                        result[i] = 'Silver Medal'
                    elif j == 2:
                        result[i] = 'Bronze Medal'
                    else:
                        result[i] = str(j + 1)
                    break

        return result


print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))
