pares = 0
n = tuple(int(input("Digite um numero: ")) for i in range(4))

print(f"A lista é: {n}")
print(f'A quantidade de vezes que o numero 9 apareceu foi de: {n.count(9)}')
if 3 in n:
    print(f"A posição do numero 3 foi: {n.index(3)}")
else:
    print("O numero 3 não apareceu na lista!")

print(f'Os numeros pares digitados foram: ', end='')
for i in n:
    if i % 2 == 0:
        print(f'{i} ', end='')



