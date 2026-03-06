val = int (input("Digite um valor: "))

conv = int (input("Digite: \n1-(Binario) \n2-(Octal)\n3-(Hexadecimal): \n"))

binario = bin(val)
octal = oct(val)
hexadecimal = hex(val)

if conv == 1:
    print("Binario: {:b}" .format(val))
elif conv == 2:
    print("Octal: {:o}" .format(val))
else:
    print("Hexadecimal: {:x}" .format(val))