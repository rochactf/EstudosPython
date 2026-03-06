import random

esc = int(input("Digite sua escolha: \n1-Pedra\n2-Papel\n3-Tesoura\nEscolha:"))

# escolha do computador
pc = random.randint(1, 3)

# mostrar escolhas em texto
if esc == 1:
    jogador = "Pedra"
elif esc == 2:
    jogador = "Papel"
else:
    jogador = "Tesoura"

if pc == 1:
    computador = "Pedra"
elif pc == 2:
    computador = "Papel"
else:
    computador = "Tesoura"

print("Você escolheu {}".format(jogador))
print("O PC escolheu {}".format(computador))

# regras do jogo
if esc == 1 and pc == 1:
    print("Empate")
elif esc == 1 and pc == 2:
    print("Computador ganhou!")
elif esc == 1 and pc == 3:
    print("Você ganhou!")

elif esc == 2 and pc == 3:
    print("Computador ganhou!")
elif esc == 2 and pc == 1:
    print("Você ganhou!")
elif esc == 2 and pc == 2:
    print("Empate!")

elif esc == 3 and pc == 1:
    print("Computador ganhou!")
elif esc == 3 and pc == 2:
    print("Você ganhou!")
elif esc == 3 and pc == 3:
    print("Empate!")