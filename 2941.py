# 심화
import sys

word = sys.stdin.readline()
word2 = word[:]

cnt = 0
if 'c=' in word:
    word2 = word.replace("c=","")
    cnt += 1
if 'c-' in word:
    word2 = word.replace("c-","")
    cnt += 1
if 'dz=' in word:
    word2 = word.replace("dz=","")
    cnt += 1
if 'd-' in word:
    word2 = word.replace("d-","")
    cnt += 1
if 'lj' in word:
    word2 = word.replace("lj","")
    cnt += 1
if 'nj' in word:
    word2 = word.replace("nj","")
    cnt += 1
if 's=' in word:
    word2 = word.replace("s=","")
    cnt += 1
if 'z=' in word:
    word2 = word.replace("z=","")
    cnt += 1

print(word2)
result = cnt + len(word2)
print(result)