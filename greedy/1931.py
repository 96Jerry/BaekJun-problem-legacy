# 그리디 알고리즘
# 가능한 많은 구간을 선택하는 문제
# 끝나는 시간을 기준으로 나열, 제일 빨리 끝나는 회의를 선택 그 시간 이후의 회의에 대해 다시 또 나열 후 선택
import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 값이 같을 때를 주의해서 기준을 x[1], x[0] 두개 잡아준다.
sorted_meetings = sorted(meetings, key = lambda x: (x[1], x[0]))

result = [sorted_meetings[0]]
criteria = sorted_meetings[0][1]
for i in range(1,n):
    # 기준에 대해서 찾아서 기준바꾸고 배열에 추가, 기준 다음 원소부터 다시 찾기
    if (criteria <= sorted_meetings[i][0]):
        criteria = sorted_meetings[i][1]
        result.append(sorted_meetings[i])

print(len(result))