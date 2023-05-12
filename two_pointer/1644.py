def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

def solve():
    N = int(input())
    primes = prime_list(N+1)
    length = len(primes)
    count = 0
    interval_sum = 0
    end = 0

    for start in range(length):
        while interval_sum < N and end < length:
            interval_sum += primes[end]
            end += 1

        if interval_sum == N:
            count += 1

        interval_sum -= primes[start]

    print(count)

solve()
