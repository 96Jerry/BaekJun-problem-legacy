# n : 전체 용액의 수
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

left, right = 0, n - 1
min_value = nums[left] + nums[right]
result = [nums[left], nums[right]]

while left < right:
    temp = nums[left] + nums[right]
    if abs(temp) < abs(min_value):
        min_value = temp
        result = [nums[left], nums[right]]
        if temp == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
