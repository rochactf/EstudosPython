n = ''
p = 0
tot = 0
prodB = ''
valB = 1000000
maisM = 0
while True:
    n = str(input("Digite o nome do produto: ")).upper().strip()
    p = int(input("Digite o valor do produto: R$"))
    tot = tot + p
    if p < valB:
        valB = p
        prodB = n
    if p > 1000:
        maisM += 1
    print("-"*80)
    e = input("Quer cadastrar mais produtos?[S/N] ").upper().strip()
    print("-" * 80)
    if e == "N":
        break


print("-"*80)
print(f"O total gasto na compra foi de: R${tot}".center(80))
print(f"A quantidade de produtos que passaram de R$1000 foi de: {maisM} produtos".center(80))
print(f"O produto mais barato foi: {prodB}".center(80))
print("-"*80)