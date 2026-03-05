valores = list()
pares = list()
impares = list()
for c in range(1, 8):
    num = int(input("Digite um valor: "))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
print('-'*30)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
