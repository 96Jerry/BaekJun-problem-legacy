# 큐
from collections import deque

a = deque()

n = int(input())

orders = []
for _ in range(n):
    orders.append(input())

answers = []
for order in orders:
    if 'push' in order:
        a.append(order.split()[1])
    elif 'pop' == order:
        if a:
            answers.append(a.popleft())
        else:
            answers.append(-1)
    elif 'size' == order:
        answers.append(len(a))
    elif 'empty' == order:
        if a:
            answers.append(0)
        else:
            answers.append(1)
    elif 'front' == order:
        if a:
            answers.append(a[0])
        else:
            answers.append(-1)
    elif 'back' == order:
        if a:
            answers.append(a[-1])
        else:
            answers.append(-1)


for answer in answers:
    print(answer)