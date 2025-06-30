"""
GERADOR DE CPFs
teste com o CPF 417.322.798-10 (417322798)
primeiro digito:
4  1  7  3  2  2  7  9  8
1  2  3  4  5  6  7  8  9
SOMATORIA = 4*1 + 1*2 + 7*3 + 3*4 + 2*5 + 2*6 + 7*7 + 9*8 + 8*9 = 4 + 2 + 21 + 12 + 10 + 12 + 49 + 72 + 72 = 254
# 254 % 11 = 1
segundo digito:
4  1  7  3  2  2  7  9  8  1
0  1  2  3  4  5  6  7  8  9
SOMATORIA = 4*0 + 1*1 + 7*2 + 3*3 + 2*4 + 2*5 + 7*6 + 9*7 + 8*8 + 1*9 = 0 + 1 + 14 + 9 + 8 + 10 + 42 + 63 + 64 + 9 = 220
# 220 % 11 = 0
"""

# Gerador de CPF
# Solicita os 9 primeiros dígitos do CPF
import os
nove_digitos = input("Digite os nove digitos do CPF (apenas números): ")
nove_digitos = nove_digitos.replace('.', '').replace('-', '').replace(' ', '')  # Remove pontos e traços
def gerar_digitos_cpf(nove_digitos):
    os.system('cls')
    nove_digitos = [int(digito) for digito in nove_digitos]
    primeiro_digito = 0
    segundo_digito = 0

    # Primeiro dígito
    for i in range(9):
        primeiro_digito += nove_digitos[i] * (i + 1)
    primeiro_digito %= 11
    if primeiro_digito >= 10:
        primeiro_digito = 0  # Se o resultado for maior ou igual a 10, o dígito é 0
    # Segundo dígito
    nove_digitos.append(primeiro_digito)
    for i in range(10):
        segundo_digito += nove_digitos[i] * i
    segundo_digito %= 11
    if segundo_digito >= 10:
        segundo_digito = 0  # Se o resultado for maior ou igual a 10, o dígito é 0
    return f"{primeiro_digito}{segundo_digito}"
print(f"CPF completo gerado: {nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{gerar_digitos_cpf(nove_digitos)}")
