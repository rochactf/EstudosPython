s = ''
i = 0
e = ''
maisD = 0
h = 0
menosV = 0
while True:
    i = int(input("Digite a idade da pessoa: "))
    s = str(input("Digite o seu sexo[M/F]: ")).upper().strip()

    if i > 18:
        maisD += 1
    if s == "M":
        h += 1
    if s == "F" and i < 20:
        menosV += 1
    e = input("Quer cadastrar nova pessoa?[S/N] ")
    if e == "N":
        break

print("-"*40)
print(f"O numero de pessoas com mais de 18 anos é de: {maisD}")
print(f"O numero de homens cadastrados foi de: {h}")
print(f"O numero de mulheres com menos de 20 anos foi de: {menosV}")
print("-"*40)