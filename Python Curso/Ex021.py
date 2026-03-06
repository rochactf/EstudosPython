somaIdade = 0
nomeV = ''
maiorH = 0
media = 0
menosM = 0
for c in range(1, 5):
    nome = str(input("Digite o nome da {}° pessoa: ".format(c))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input("Digite o sexo da {}° pessoa [M/F]: ")).strip()
    somaIdade += idade
    if c ==1 and sexo in 'Mm':
        maiorH = idade
        nomeV = nome
    if sexo in 'Mm' and idade > maiorH:
        maiorH = idade
        nomeV = nome
    if sexo in 'Ff' and idade < 20:
        menosM =+ 1

media = somaIdade / 4
print("A medida de idade do grupo é de: {}".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maiorH, nomeV))
print("O numero de mulheres com menos de 20 anos é de: {}".format(menosM))
