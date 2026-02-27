s = ''

while s != 'S':
    s = str(input("Digite seu sexo: [M/F], digite S para parar: ")).strip().upper()
    if s != 'F' and s != 'M':
        print("Digite apenas M ou F!")
