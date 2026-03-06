from random import randint
s = 0
v = 0
d = 0
print('-'*65)
print("Vamos começar o jogo(Par ou Impar)".center(65))
print('-'*65)
while True:
    pc = randint(0, 1000)
    j = int(input("Digite um numero inteiro (Digite numero negativo para encerrar): "))
    if j < 0:
        break
    e = input("Par ou Impar: ").lower()
    pc = randint(0, 10)
    s = j + pc
    if e == "par":
        if s % 2 == 0:
            print(f"O PC escolheu o numero: {pc}")
            print(f"Soma: {s}")
            print("Você ganhou!")
            v += 1
        else:
            print(f"O PC escolheu o numero: {pc}")
            print(f"Soma: {s}")
            print("Você perdeu!")
            d += 1
    if e == "impar":
        if s % 2 == 0:
            print(f"O PC escolheu o numero: {pc}")
            print(f"Soma: {s}")
            print("Você perdeu!")
            d += 1
        else:
            print(f"O PC escolheu o numero: {pc}")
            print(f"Soma: {s}")
            print("Você ganhou!")
            v += 1

print("-"*65)
print("O jogo acabou!".center(65))
print(f"Você ganhou {v} vezes e perdeu {d} vezes.".center(65))
if v > d:
    print("Parabéns você é otimo nisso!".center(65))
else:
    print("Não foi dessa vez!".center(65))
print("-"*65)