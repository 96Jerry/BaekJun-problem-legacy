# 재귀
# 별 찍기
def solution(n):
    if n == 3:
        return ['***','* *','***']
    new_n = n // 3
    l = []
    stars = solution(new_n)
    for star in stars:
        l.append(star*3)
    for star in stars:
        l.append(star + ' '*(new_n) + star)
    for star in stars:
        l.append(star*3)
    
    return l

n = int(input())
print(*solution(n), sep='\n')