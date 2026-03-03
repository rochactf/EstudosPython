from random import randint
c = 0

numeros = tuple(randint(1,10) for i in range(5))

while c < len(numeros):
    if c == 0:
        maior = menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
    c += 1
print(f'Os numeros sorteados foram: {numeros}' )
print(f'O menor numero é: {menor}')
print(f'O maior numero é: {maior}')
