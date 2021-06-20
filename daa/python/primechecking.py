import math
def isPrime(num,div):
    if div == 1 or  div == 0 :  return True
    if(num % div == 0): return False
    return isPrime(num, div - 1)
# for i in range(1,10000):
#     if not  isPrime((i * i) + i + 41, int(i / 2)) : print(i)
def primeSieve(n):
    primes = [1] * (n + 1)
    primes[0],primes[1] = 0,0
    for i in range(2,int(math.sqrt(n))):
        if primes[i] == 1:
            j = 2
            while i * j <= n : 
                primes[i * j] = 0
                j += 1
    return primes
a = primeSieve(100)
for i in range(0,len(a)):
    if a[i] == 1 :
        print(i,end=" ")
print('')
print(len(a))