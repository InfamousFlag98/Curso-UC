"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

"""

max_attempts = 3
tentativas = 0

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

while (not nome or not idade) and tentativas < max_attempts:
    if not nome:
        print('Nome não pode ser vazio.')
    if not idade:
        print('Idade não pode ser vazia.')
    tentativas += 1
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém espaços: {" " in nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Número máximo de tentativas atingido. Encerrando o programa.')