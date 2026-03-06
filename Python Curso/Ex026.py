a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))
c = 1

while c < 11:
    termo = a1 + (c -1) * r
    print("{} " .format(termo), end = "")
    c += 1