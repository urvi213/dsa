"""n = 10
sum=0
for i in range(n):
    sum+= i+1
print(sum)"""

def sum(n):
    if n == 1: return 1
    else: return n + sum(n-1)   
print(sum(5))


def fibonaaci(n):
    if n == 0 or n == 1: return n
    else: return(fibonaaci(n-1)+fibonaaci(n-2))
print(fibonaaci(20))