# 백트래킹, dfs
# N-Queen
def is_safe(row, col, board):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def dfs(n, board, col):
    if col == n:
        return 1
    count = 0
    for row in range(n):
        if is_safe(row, col, board):
            board[col] = row
            count += dfs(n, board, col + 1)
    
    return count

def n_queen(n):
    board = [-1] * n
    return dfs(n, board)

n = int(input())
print(n_queen(n))

#  board[i] = j
#  board의 i열에서 j행의 위치에 퀸이 있다.