# 심화
word = input().lower()
cnt = [0] * 26

for i in range(len(word)):
    cnt[ord(word[i])-ord('a')] += 1

c = cnt.count(max(cnt))
if c >1 :
    print('?')
else:
    print(chr(cnt.index(max(cnt))+ord('a')).upper())