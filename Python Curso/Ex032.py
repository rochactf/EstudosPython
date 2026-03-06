s = cont = n = 0

while True:
    n = int(input("Digite um numero para tabuada (Digite um numero negativo para encerrar): "))
    if n < 0:
        break
    cont = 0
    while cont < 10:
        s = n * cont
        cont += 1
        print(f"{n} x {cont} = {s}")

print("FIM DO PROGRAMA")