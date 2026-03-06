r1 = int(input("Qual o valor da primeira reta: "))
r2 = int(input("Qual o valor da segunda reta: "))
r3 = int(input("Qual o valor da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("Triangulo equilatero, todas os lados iguais.")

    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("Triagulo isoceles, apenas 2 lados iguais.")

    else:
        print("Triangulo escaleno, os 3 lados são diferentes.")
