# 브루트 포스
# 모든 경우를 시도하여 N의 생성자를 구하는 문제
n = int(input())

answer = []
for i in range(n):
    x = str(n - i)
    total = 0
    for j in range(len(x)):
        total += int(x[j])
    if i == total:
        answer.append(n-i)
if answer:
    print(min(answer))
else:
    print(0)