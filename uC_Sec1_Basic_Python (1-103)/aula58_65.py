"""
cond = True
while cond:
    nome = input('Digite seu nome: ')
    print(f'Olá {nome}')
    if nome == 'sair':
        break
"""
qtd_linhas = 6
qtd_colunas = 6

linha = 0
while linha <= qtd_linhas:
    coluna = 0
    while coluna <= qtd_colunas:
        print(f'Linha: {linha}, Coluna: {coluna}')
        coluna += 1
    linha += 1

print('Fim do programa')