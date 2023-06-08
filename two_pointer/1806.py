# 수열에서 연속된 수들의 합이 s 이상이 것 중에서 길이가 제일 짧은 것들의 길이 구하기
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 연속한 부분 수열을 모두구해서 합이 15 이상인것들을 추려낸다.
# 2. 15이상인 것들 중 길이가 제일 짧은 것의 길이를 구한다.
# n = 10만, s = 1억
# 입력이 크기때문에 시간이 너무 오래걸린다.

partial_sum = 0
start, end = 0, 0
min_length = float('inf')

while end <= n:
    if partial_sum >= s:
        min_length = min(min_length, end-start)
        partial_sum -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        partial_sum += arr[end]
        end += 1
if min_length != float('inf'):
    print(min_length)
else:
    print(0)