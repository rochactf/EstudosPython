c = 0
maior = 0

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
while c != 5:
    print('-'*5, 'ESCOLHA UMA OÇÃO', '-'*5)
    c = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\nOpção: '))
    if c == 1:
        s = n1+n2
        print("O valor da soma desses 2 numeros é de: {}".format(s))
    elif c == 2:
        s = n1*n2
        print("O valor da multiplicaçao desses dois numero é de: {}".format(s))
    elif c == 3:
        if n1 > n2:
            maior = n1
            print("O maior numero é: {}".format(maior))
        else:
            maior = n2
            print("O maior numero é {}".format(maior))
    elif c == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))

print('-'*30)
print('        FIM DO PROGRAMA')
print('-'*30)

