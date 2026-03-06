menor = 0
maior = 0
for c in range(1, 7+1):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if 2026 - ano < 18:
        menor += 1
    else:
        maior += 1

print("O numero de pessoas maiores de idade é {}" .format(maior))
print("O numero de pessoas menores de idade é {}" .format(menor))