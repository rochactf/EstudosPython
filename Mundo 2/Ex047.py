lista = []
listaA = []
listaB = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        listaA.append(num)
    if num % 2 == 1:
        listaB.append(num)
    resp = input("Deseja continuar? [S/N] ").strip().upper()
    if resp == "N":
        break

print("=-"*30)
print(f"Os valores digitados foram: {lista}")
print(f"Os valores pares digitados foram: {listaA}")
print(f"Os valores impares digitados foram: {listaB}")
print("=-"*30)