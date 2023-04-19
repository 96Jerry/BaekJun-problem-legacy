# 집합과 맵
# 카드의 집합을 만들어 특정 카드가 집합에 있는지 빠르게 찾는 문제

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
shows = list(map(int, input().split()))

for show in shows:
    if show in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')