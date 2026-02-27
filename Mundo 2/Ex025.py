
"""COM WHILE
n = int(input('Digite um numero: '))
f = 1
c = n
while c > 0:
    f *= c
    c -= 1

print("O fatorial de {} é {}".format(n, f))"""


#COM FOR
n = int(input('Digite um numero: '))
f = 1
c = n
for c in range(1, n + 1):
    f *= c
print("O fatorial de {} é {}".format(n, f))