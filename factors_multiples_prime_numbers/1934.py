# 약수, 배수, 소수
# 유클리드 호제법
t = int(input())

def gcd(a,b):
    while b:        
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

arr=[]
for _ in range(t):
    arr.append(list(map(int, input().split())))

for i in range(t):
    print(lcm(*arr[i]))