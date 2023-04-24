# 백트래킹
# 스도쿠
sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

def is_safe(x,y,num,sudoku):
    for i in range(9):
        if sudoku[x][i] == num or sudoku[i][y] == num:
            return False
    a = (x // 3) * 3
    b = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[a+i][b+j] == num:
                return False
    return True


def solution(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1,10):
                    if is_safe(i,j,k,sudoku):
                        sudoku[i][j] = k
                        if solution(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return True

solution(sudoku)
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end=' ')
    print()