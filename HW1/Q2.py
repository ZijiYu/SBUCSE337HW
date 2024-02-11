def is_balanced(s):
    dic = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for item in s:
        if item in dic:
            stack.append(item)
        elif stack and dic[stack[-1]] == item:
            stack.pop()
        else:
            return False
    return len(stack) == 0
