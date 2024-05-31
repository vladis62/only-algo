class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        result = {}

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                result[arr[i] / arr[j]] = (arr[i], arr[j])

        result = dict(sorted(result.items()))
        for _, value in result.items():
            if k == 1:
                return list(value)
            k -= 1


print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], k=3))
print(Solution().kthSmallestPrimeFraction([1, 7], k=1))
