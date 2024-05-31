def get_number_of_good_pairs(numbers) -> int:
    remainder = [0] * 200
    for num in numbers:
        remainder[num % 200] += 1

    count = 0
    for r in remainder:
        if r > 1:
            count += r * (r - 1) // 2
    return count


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
