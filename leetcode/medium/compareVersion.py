class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')
        n_v1 = len(version1)
        n_v2 = len(version2)

        if n_v1 > n_v2:
            version2 += ['0'] * (n_v1 - n_v2)
        if n_v1 < n_v2:
            version1 += ['0'] * (n_v2 - n_v1)

        print(version1)
        print(version2)

        for i in range(len(version1)):
            num1 = int(version1[i])
            num2 = int(version2[i])

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        return 0

print(Solution().compareVersion('1', '1.1'))
