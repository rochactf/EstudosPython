n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota:"))

med = (n1 + n2) / 2
if med < 5.0:
    print("Reprovado")
elif med >= 5.0 and med <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")