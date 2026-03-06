n = s = t = 0
while True:
    n = int(input("Digite um numero inteiro (Digite [999] para parar): "))
    if n == 999:
        break
    s += n
    t += 1
print(f"A soma desses numeros é de {s} e o total de numeros digitados é de {t}")
