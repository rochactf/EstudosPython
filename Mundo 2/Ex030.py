r = 'S'
valT = 0
m = 0
s = 0

while r != 'N':
    n = int(input('Digite um numero inteiro: '))

    if valT == 0:
        maior =  menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    s += n
    valT += 1

    r = str(input('Quer continuar? [S/N] ')).strip().upper()

m = s / valT

print("O menor numero digitado foi {}".format(menor))
print("O maior numero digitado foi {}".format(maior))
print("A media dos numeros digitados foi {:.2f}".format(m))


