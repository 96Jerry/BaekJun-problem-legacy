# 일반수학 1
# 분수의 순서에서 규칙을 찾는 문제
x = int(input())

now = 0
i = 1
while now < x:
    now += i
    i += 1

a = x - now + i - 1
if (i-1) % 2 == 0:
    print(f"{a}/{i-a}")
else:
    print(f"{i-a}/{a}")
