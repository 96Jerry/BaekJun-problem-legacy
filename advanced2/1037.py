# 심화 2
# 진짜 약수 => 원래 수 구하기
def solution(arr):
    arr.sort()
    if len(arr) == 1:
        return arr[0]**2
    return arr[-1]*arr[0]
    


n = int(input())
a = list(map(int, input().split()))

print(solution(a))