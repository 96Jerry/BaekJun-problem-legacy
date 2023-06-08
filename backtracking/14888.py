# 백트래킹
# 연산자 끼워넣기
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

def solution(depth,total, plus, minus, multiple, devide):
    global minimum, maximum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        solution(depth+1,total+nums[depth], plus-1,minus,multiple,devide)
    if minus:
        solution(depth+1,total-nums[depth], plus,minus-1,multiple,devide)
    if multiple:
        solution(depth+1,total*nums[depth], plus,minus,multiple-1,devide)
    if devide:
        solution(depth+1,int(total/nums[depth]), plus,minus,multiple,devide-1)

maximum, minimum = float('-inf'), float('inf')
solution(1,nums[0], ops[0],ops[1],ops[2],ops[3])

print(maximum)
print(minimum)