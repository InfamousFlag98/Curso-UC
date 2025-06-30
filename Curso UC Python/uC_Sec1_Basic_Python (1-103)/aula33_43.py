# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')
"""
# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
entrada = input('[E]ntrada ou [S]aida: ')
senha = input('Senha: ')
if senha == '123456' and entrada == 'E':
    print('Você está entrando')
elif senha == '123456' and entrada == 'S':
    print('Você está saindo')
elif senha != '123456' and entrada == 'E':
    print('Senha incorreta, tente novamente')
elif senha != '123456' and entrada == 'S':
    print('Senha incorreta, tente novamente')
elif senha == '123456' and entrada != 'E' and entrada != 'S':
    print('Entrada ou saída inválida')
else:
    print('Opção inválida')

    
    """