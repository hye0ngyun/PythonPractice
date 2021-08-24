def prime(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
    return n if isPrime else 0

def oneToN(n):
    total = 0
    for i in range(1, n+1):
        total += prime(i)
    return total


n = int(input())
total = oneToN(n)
print(total)

