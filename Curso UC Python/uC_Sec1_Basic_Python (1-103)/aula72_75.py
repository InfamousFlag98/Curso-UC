
senha_salva = '123456'
senha = input('Digite a senha: ')
repetições = 0
while senha != senha_salva:
    print('Senha incorreta!')
    senha = input(f'Digite a senha ({repetições}x): ')
    repetições += 1


texto = 'Python é uma linguagem de programação incrível!'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

#For + Range
#range -> range(start, stop, step)

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
