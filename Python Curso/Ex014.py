n = int(input("Digite o numero da tabuada: "))

for c in range(1, 11):
    s = n * c
    print("{} x {} = {}" .format(n, c, s))