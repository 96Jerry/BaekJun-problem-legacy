# 재귀
# 하노이탑
def solution(arr, n, start, end, via):
    if n == 1:
        arr.append((start, end))
        return
    
    solution(arr,n-1, start, via, end)
    arr.append((start, end))
    solution(arr, n-1, via, end, start)
    

n = int(input())
arr = []
solution(arr, n, 1, 3, 2)
times = len(arr)
print(times)
for _ in range(times):
    print(f"{arr[_][0]} {arr[_][1]}")

# def solution(n, a, b):
#     if n == 1:
#         return f"{a} {b}"
#     c = 6 - a - b
#     return solution(n-1, a, c) + solution(1, a, b) + solution(n-1,c,b)