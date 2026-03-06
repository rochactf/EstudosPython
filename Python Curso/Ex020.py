menor = 0
maior = 0
for c in range(1, 6):
    peso = int(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("O maior peso entre elas é de: {}".format(maior))
print("O menor peso entre elas é de: {}".format(menor))
