def is_correct_bracket_seq(brackets):
    open_to_closed_bracket = {'(': ')', '[': ']', '{': '}'}
    open_bracket = ['(', '[', '{']
    if not len(brackets):
        return True
    stack = []
    for bracket in brackets:
        if bracket in open_bracket:
            stack.append(bracket)
            continue
        if len(stack) == 0:
            return False
        prev_bracket = stack.pop()
        if not len(stack) and bracket != open_to_closed_bracket[prev_bracket]:
            return False

    return len(stack) == 0


def main():
    n = input()
    print(is_correct_bracket_seq(n))


if __name__ == '__main__':
    main()
