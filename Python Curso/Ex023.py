from random import randint

print('-'*60)
print("Vou pensar em um numero inteiro de 0 a 5, tente adivinhar...")
print('-'*60)

n = randint(0, 5)
p = int(input('Digite um numero entre 0 e 5: '))

while p != n:
    p = int(input('Você errou tente novamente.: '))

print("Parabens você acertou!")