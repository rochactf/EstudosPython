a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))

c = 1
mais = 10
total = 10

while c < 11:
    termo = a1 + (c - 1) * r
    print("{} ".format(termo), end="")
    c += 1

m = int(input("\nQuantos termos a mais deseja mostrar: "))
while m != 0:
    total += m
    while c <= total:
        termo = a1 + (c - 1) * r
        print("{} ".format(termo), end="")
        c += 1

    m = int(input("\nQuantos termos a mais deseja mostrar: "))
print("Programa finalizado com total de {} termos".format(total))

