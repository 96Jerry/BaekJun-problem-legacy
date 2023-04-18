# 일반 수학 1
# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제
n = int(input())

def qqq(n):
    if n == 1:
        return 1
    
    a = (n-2) // 6
    for i in range(a+1):
        a -= i
        if a < 0:
            return i+1
        elif a == 0:
            return i+2



print(qqq(n))