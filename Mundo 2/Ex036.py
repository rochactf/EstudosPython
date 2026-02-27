valor = int(input("Digite o valor a ser sacado: R$"))

ced = 50
totalCed = 0

print("-"*30)
print("CEDULAS ENTREGUES:")

while True:
    if valor >= ced:
        valor -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f"{totalCed} cédulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else:
            break
        totalCed = 0
print("-"*30)
