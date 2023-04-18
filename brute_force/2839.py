# 브루트 포스
import math
n = int(input())

a = math.floor(n / 5)

while a >= 0:
    rest = n - a*5
    if rest % 3 == 0:
        result = rest // 3 + a
        break
    a -= 1

if a < 0:
    print(-1)
else:
    print(result)