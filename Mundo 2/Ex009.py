prod = float(input("Digite o valor do produto: "))
cond = int(input("Digite a forma de pagamento:\n1-A vista dinheiro ou pix.\n2-A vista cartão.\n3-Em até 2x.\n4-3x ou mais 20% de juros.\nDigite:"))


if cond == 1:
    prod = prod - (prod * 0.10)
    print("Valor do produto: {:.2f}" .format(prod))
elif cond == 2:
    prod = prod - (prod * 0.05)
    print("Valor do produto: {:.2f}" .format(prod))
elif cond == 3:
    print("Valor do produto: {:.2f}" .format(prod))

else:
    prod = prod + (prod * 0.20)
    print("Valor do produto: {:.2f}" .format(prod))