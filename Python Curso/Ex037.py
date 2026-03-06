numero = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    esc = int(input("Digite um numero entre 0 e 20: "))
    if esc < 0 or esc > 20:
        continue
    else:
        break

print(f'Você digitou o numero {numero[esc]}' )