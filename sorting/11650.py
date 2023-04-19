# 정렬
# 좌표 정렬하기
n = int(input())

arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

for _ in range(n):
    print(arr[_][0], arr[_][1])