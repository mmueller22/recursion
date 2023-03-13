def produkt(n):
    if n == 3:
        return n
    else:
        return produkt(n-1) * n
def summe(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + summe(n-1)
    else:
        return summe(n-1)
def produkt_adv(n):
    if n == 1:
        return 1
    elif n % 2 != 0:
        return n * produkt_adv(n-1)
    else:
        return produkt_adv(n-1)
def reduzieren(n):
    if n == 0:
        return 100
    else:
        return 0.7 * reduzieren(n-1)
def fib(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)    
#print(produkt(5))
#print(summe(6))    
#print(produkt_adv(7))
#print(reduzieren(3))
#print(fib(8))