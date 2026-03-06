n = int(input("Digite um numero inteiro: "))

if n < 2:
    print("Não é primo!")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("Primo!")
    else:
        print("Não é primo!")