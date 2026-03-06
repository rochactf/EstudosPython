n = 0
t = 0
s = 0
while n != 999:
    n = int(input('Digite um valor, digite [999] para encerrar: '))
    if n != 999:
        s += n
        t += 1
    else:
        print("O total de numero digitados foi de {} e a soma desses numero é : {}".format(t, s))