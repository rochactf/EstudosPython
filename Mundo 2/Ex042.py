palavras = ('Python', 'Java', 'Programar', 'Estudos', 'Tupla')

for palavra in palavras:
    vogais = ''
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += letra + ''
    print(f"Na palavra {palavra} temos: {vogais}")