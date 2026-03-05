valores = []

while True:
    num = int(input("Digite um valor: "))
    if num in valores:
        print("Valor já adicionado, tente outro!")
    else:
        valores.append(num)
        print(f"Valor adicionado com sucesso!")

    resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp in "N":
        break
valores.sort()
print("-"*70)
print(f"Os valores digitados em ordem crescente foram: {valores}")
print("-"*70)