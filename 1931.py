# 그리디 알고리즘
# 회의실 배정
# 한개의 회의실. 여러 회의의 시작시간과 끝나는시간이 주어짐.
# 겹치지 않으면서 회의실을 사용할 수 있는 회의의 최대 개수는?
# (시작 끝 시간이 같을 수도 있다.)
import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
# print(a)
# n = 11
# a = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
``