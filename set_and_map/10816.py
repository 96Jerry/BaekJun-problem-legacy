# 집합과 맵
# 각 카드의 개수를 찾는 문제
a = {}
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
shows = list(map(int, input().split()))

for card in cards:
    if card in a.keys():
        a[card] += 1
    else:
        a[card] = 1

for show in shows:
    if show not in a.keys():
        print(0, end=' ')
    else:
        print(a[show], end=' ')