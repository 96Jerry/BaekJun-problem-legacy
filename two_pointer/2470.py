n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left = 0
right = n - 1
min_value = abs(solutions[left] + solutions[right])
result = (solutions[left], solutions[right])

while left < right:
    temp = solutions[left] + solutions[right]
    if abs(temp) < min_value:
        min_value = abs(temp)
        result = (solutions[left], solutions[right])
        if temp == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
