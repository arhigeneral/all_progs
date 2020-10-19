#Найдите сумму всех простых чисел меньше двух миллионов.
def eratosthen(n):
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
        print(i)
        for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

print(sum(eratosthen(10)))
