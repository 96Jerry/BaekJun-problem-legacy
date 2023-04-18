# 브루트 포스
# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제
def check_board(x,y,board):
    color1 = ['W','B']*4
    color2 = ['B','W']*4
    color = [color1,color2]

    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if board[x+i][y+j] != color[i%2][j]:
                cnt1 += 1
            if board[x+i][y+j] != color[(i+1)%2][j]:
                cnt2 += 1
    return min(cnt1, cnt2)



n, m = map(int, input().split())

board = [input() for _ in range(n)]

min_change = float('inf')
for x in range(n-7):
    for y in range(m-7):
        change = check_board(x,y,board)
        min_change = min(change, min_change)

print(min_change)
