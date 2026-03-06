galera = list()
dado = list()
maisP = menosP = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input("Peso: ")))

    if len(galera) == 1:
        maisP = menosP = dado[1]
    else:
        if dado[1] > maisP:
            maisP = dado[1]
        if dado[1] < menosP:
            menosP = dado[1]

    galera.append(dado[:])
    dado.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*60)
print(f'Ao total foram cadastrado {len(galera)} pessoas')

print(f'O maior peso foi de {maisP}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maisP:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {menosP}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menosP:
        print(f'[{p[0]}] ', end='')
print()
print('-'*60)