# 심화
import sys

def is_group_word(word):
    visited = set()
    prev_word = word[0]
    visited.add(prev_word)
    for i in word[1:]:
        if i != prev_word:
            if i in visited:
                return False
            else:
                visited.add(i)
                prev_word = i
    return True

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(sys.stdin.readline())
cnt = 0

for word in words:
    if is_group_word(word):
        cnt += 1
print(cnt)
