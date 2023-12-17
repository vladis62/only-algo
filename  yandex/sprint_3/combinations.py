def generate_combinations(digits):
    if not digits:
        return []

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    backtrack(0, [])
    return combinations


def main():
    print(*generate_combinations('27'))


if __name__ == '__main__':
    main()
