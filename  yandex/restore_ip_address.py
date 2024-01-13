# 172162552 -> 172.16.255.2

# 172162552 -> 17.216.255.2


def restore_address(s):
    result = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                result.append(s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:])

def isValidAddress(address):
    return address.split('.')


nums = [1, 2, 3, 5, 11, 3, 111, 7, 27]

for n in nums:
    if n < 5:
        nums.remove(n)

print(nums)
