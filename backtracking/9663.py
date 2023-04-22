# 백트래킹
# n-queen
def is_safe(col, row, boards):
    for i in range(row):
        if boards[i] == col or abs(boards[i]-col) == abs(i-col):
            return False
    return True

def dfs(n, count, row, boards):
    if row == n:
        count += 1
        return count
    for col in range(n):
        if is_safe(col, row, boards):
            boards[row] = col
            count = dfs(n, count, row+1, boards)
    return count


def n_queen(n):
    boards = [-1] * n
    dfs(n, boards)

n = int(input())
print(n_queen(n))