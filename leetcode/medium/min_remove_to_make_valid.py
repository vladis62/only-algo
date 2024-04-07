class Solution:
    def minRemoveToMakeValid(self, s):
        n = len(s)
        result = [''] * n
        cnt = 0

        for i in range(n):
            if s[i] == '(':
                result[i] = s[i]
                cnt += 1
            elif s[i] == ')':
                if cnt == 0:
                    result[i] = '*'
                else:
                    result[i] = s[i]
                    cnt -= 1
            else:
                result[i] = s[i]
        print(result)

        for i in range(n - 1, -1, -1):
            if s[i] == '(' and cnt > 0:
                result[i] = '*'
                cnt -= 1

        return ''.join(list(filter(lambda ch: ch != '*', result)))


# print(Solution().minRemoveToMakeValid('lee(t(c)o)de)'))
# print(Solution().minRemoveToMakeValid('))(('))
# print(Solution().minRemoveToMakeValid('aa(aa(asd(a))((aaa)'))
