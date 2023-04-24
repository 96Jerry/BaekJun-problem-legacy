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