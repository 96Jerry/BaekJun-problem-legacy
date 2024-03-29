# 부분구간 합
# 구간 합의 아이디어를 응용하여 특정 조건을 만족하는 구간의 개수를 구하는 문제
import sys

# 파이썬은 default 입력을 문자열로 받는다.
n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))


# sum1 은 부분합 리스트
sum1 = [0]*(n+1)
for i in range(1, len(array)+1):
    sum1[i] = sum1[i-1] + array[i-1]


# prefix는 sum1을 m으로 나눈 나머지
# 혹은 prefix[r] 을 나머지가 r인 부분합의 개수로 지정해준다.
prefix = [0]*(m+1)
for i in range(len(sum1)):
    r = sum1[i]%m
    prefix[r] += 1 # 추가됨


# # prefix에서 0,1,2, ... , n-1 을 찾은 후 나머지가 같은 배열값들끼리 조합 경우의 수를 계산한다.
# # combination 계산 = i*(i+1)/2
# result = []
# for i in range(m):
#     count = 0
#     for j in range(n+1):
#         if prefix[j] == i:
#             count += 1
#     result.append(count*(count-1)//2)
# # print(result)
# print(sum(result))

result = []
for i in range(len(prefix)):
    if (prefix[i] != 0):
        l = prefix[i]
        result.append(l*(l-1)//2)
print(sum(result))