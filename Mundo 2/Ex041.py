lista = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90, 'Estojo', 25.0, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.90, 'Livro', 34.90)

print("-"*40)
print("LISTAGEM DE PREÇOS".center(40))
print("-"*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print("-"*40)
