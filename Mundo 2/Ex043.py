valores = []
menor = maior = 0

for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if c == 0:
        menor = valores[c]
        maior = valores[c]
    elif valores[c] > maior:
        maior = valores[c]

    elif valores[c] < menor:
        menor = valores[c]

print("-"*65)
print(f"Você digitou os valores {valores}")

print(f"O menor valor dessas lista foi: {menor} na(s) posição -> ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end='')

print(f"\nO maior valor dessa lista foi: {maior} na(s) posição -> ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end='')
print()
print("-"*65)

