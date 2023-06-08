<<<<<<< HEAD
n = int(input())

def dfs(next_queen, queens, cases, n):
        # 같은 행이면 리턴
        if next_queen in queens:
            return
        # 대각선이면 리턴
        for row, column in enumerate(queens):
            if (len(queens)-row)==abs(next_queen-column):
                return
        queens.append(next_queen)
        if len(queens) == n:
            cases[0] += 1
            return
        for next_queen in range(n):
            dfs(next_queen, queens[:], cases, n)

def solution(n):
    cases = [0]
    for next_queen in range(n):
        queens=[]
        dfs(next_queen, queens, cases, n)
    return cases[0]

print(solution(n))
=======
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
>>>>>>> 42d30224db2d459a1772c388571811566ab23778
