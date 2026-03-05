lista = []
esta = ''

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    resp = (input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if 5 in lista:
        esta = 'Sim!'
    else:
        esta = 'Não!'
    if resp == "N":
        break
lista.sort(reverse=True)
print("=-"*55)
print(f"A quantidade de numeros digitados na lista foram de: {len(lista)} elementos.")
print(f"A lista em ordem decrescente é: {lista}")
print(f"O numero 5 está na lista?: {esta}")