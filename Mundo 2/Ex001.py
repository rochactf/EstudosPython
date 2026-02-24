sal = int (input('Digite seu salario: '))
casa = int (input('Digite o valor da casa: '))
anos = int (input('Digite em quantos anos você quer parcelar: '))

prestacao = casa / (anos *12)

if prestacao >= sal * 0.30:
    print("O valor da prestacao ultrapassa 30% do seu salario")
    print("Valor da prestacao {:.2f}".format(prestacao))
else:
    print("O valor da prestacao esta de acordo com seu salario")
    print("Valor da prestacao {:.2f}" .format(prestacao))