from numba import jit

@jit
def prime(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
          n /= i
          table.append(i)
    i += 1

    if n > 1:
        table.append(n)

    return table

n = prime(600851475143)
print(max(n))
