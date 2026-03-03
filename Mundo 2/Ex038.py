tabela = ("Palmeiras", "São Paulo", "Corinthians", "Bahia", "Fluminense", 'Atletico_PR', 'Bragantino', 'Gremio', 'Chapecoense', 'Mirassol', 'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'Vitoria', 'Remo', 'Atletico-MG','Internacional', 'Cruzeiro', 'Vasco')

print(f"Os cinco primeiros colocados da tabela são: {tabela[0:5]}")
print(f"Os quatro ultimos colocados da tabela são: {tabela[16:20]}")
ordenada = sorted(tabela)
print(f"A tabela em ordem alfabetica é: {ordenada}")
pos = tabela.index('Chapecoense')
print(f'A Chapecoense está em: {pos + 1}° lugar')
print(f"O primeiro colocado é: {tabela[0]}" )