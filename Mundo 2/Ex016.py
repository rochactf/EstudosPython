a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))

for c in range(1, 11):
    termo = a1 + (c -1) * r
    print("{} " .format(termo), end = "")