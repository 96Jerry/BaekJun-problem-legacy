# 그리디 알고리즘
# 동전 0
import sys

n, k = map(int, sys.stdin.readline().split())
# print(n, k)
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
# print(a)

# 주어진 k 값보다 작은 a 안의 최대 값을 찾는다. 그 값부터 제일 작은값까지 루프를 돌면서
# 최대로 쓸 수 있는 개수를 확인한다. 그 개수를 모두 더해준다.
a.reverse()
total = 0
for el in a:
    if el <= k:
        number = k // el
        total += number
        k = k - el * number
print(total)
