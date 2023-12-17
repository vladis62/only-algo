def cookies(children, cookies):
    children = sorted(children)
    cookies = sorted(cookies)
    sum = 0
    idx = 0
    for child in children:
        while idx < len(cookies) and cookies[idx] < child:
            idx += 1
        if idx < len(cookies):
            sum += 1
            idx += 1
    return sum


def main():
    _ = int(input())
    children = list(map(int, input().split(' ')))
    _ = int(input())
    cookie = list(map(int, input().split(' ')))
    sum = cookies(children, cookie)
    print(sum)


if __name__ == '__main__':
    main()
