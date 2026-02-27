n = int(input('Digite quantos termos a sequencia deve ter: '))

t1 = 0
t2 = 1
c =1

while c <= n:
    print(t1, end=' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
