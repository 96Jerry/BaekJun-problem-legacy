# 정렬
# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬(stable sort)
from collections import defaultdict
n = int(input())

a = defaultdict(list)
for i in range(n):
    user = input().split()
    a[int(user[0])].append((i, user[1]))

b = sorted(a.items(), key=lambda x: (x[0], x[1][0]))

for i in range(len(b)):
    for j in range(len(b[i][1])):
        print(b[i][0], end=' ')
        print(b[i][1][j][1])