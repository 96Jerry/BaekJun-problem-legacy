# 정렬
# 단어 정렬
from collections import defaultdict
n = int(input())

a = defaultdict(list)
for _ in range(n):
    temp = input()
    if temp not in a[len(temp)]:
        a[len(temp)] += [temp]

b = sorted(a.items(), key=lambda x: x[0])

for i in range(len(b)):
    b[i][1].sort()
    for j in b[i][1]:
        print(j)