frase = input("Digite uma frase: ").strip().lower()
frase = frase.replace(" ", "")

if frase == frase[::-1]:
    print("É palindromo")
else:
    print("Não é palindromo")