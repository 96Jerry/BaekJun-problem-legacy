# 스택
# 스택 만들기
def solution(stack, order):
    if 'push' in order:
        stack.append(order.split()[1])
        return
    elif 'pop' == order:
        if stack:
            return stack.pop()
        return -1
    elif 'size' == order:
        return len(stack)
    elif 'empty' == order:
        if stack:
            return 0
        return 1
    elif 'top' == order:
        if not stack:
            return -1
        return stack[-1]



n = int(input())
arr = []
answer = []
for _ in range(n):
    result = solution(arr, input())
    if result != None:
        answer.append(result)
for _ in range(len(answer)):
    print(answer[_])

