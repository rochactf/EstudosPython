from random import randint
s = 0
v = 0
d = 0
print('-'*65)
print("Vamos começar o jogo(Par ou Impar)".center(65))
print('-'*65)
while True:
    pc = randint(0, 10)
    j = int(input("Digite um numero inteiro (Digite numero negativo para encerrar): "))
    e = input("Par ou Impar: ").lower().strip()


    if e != "impar" and e != "par":
        print("Escolha invalida! Digite somente 'Par' ou 'Impar'.\n")
        continue
    s = j + pc

    if(s % 2 == 0 and e== "par") or (e == "impar" and s % 2 != 0):
        print("Você ganhou!")
        print("Vamos jogar novamente...")
        v = v + 1
    else:
        print("Você perdeu!")
        break

print("-"*65)
print("O jogo acabou!".center(65))
print(f"Você ganhou {v} vezes consecutivas.".center(65))
print("Parabéns você é otimo nisso!".center(65))
print("-"*65)