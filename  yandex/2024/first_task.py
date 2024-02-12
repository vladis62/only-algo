def is_palindrome(s):
    return s == s[::-1]


def count_palindromes(n, m):
    count = 0
    fill = max(len(str(n)), len(str(m)))
    for hour in range(n):
        hour_str = str(hour).zfill(fill)
        for minute in range(m):
            minute_str = str(minute).zfill(fill)
            time_str = hour_str + ":" + minute_str
            print(time_str)
            if is_palindrome(time_str):
                count += 1
    return count


def main():
    n, m = list(map(int, input().split()))
    print(count_palindromes(n, m))


if __name__ == '__main__':
    main()
