ano = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano

if idade > 18:
    print("Já passou do tempo do alistamento")
elif idade < 18:
    print("Você ainda nao precisa se alistar")
else:
    print("Você precisa se alistar neste ano")
