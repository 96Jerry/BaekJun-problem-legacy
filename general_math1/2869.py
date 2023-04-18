# 일반 수학 1
# 달팽이의 움직임을 계산하는 문제
import sys, math

a, b, v = map(int, sys.stdin.readline().split())

x = (v-a) / (a-b)
x = math.ceil(x)
print(x+1)