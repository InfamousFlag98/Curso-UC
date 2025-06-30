num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')
op = input('Digite a operação (+, -, *, /): ')
num_validos = None
op_validas = ['+', '-', '*', '/']

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    try:
        num1 = float(num_1)
        num2 = float(num_2)
    except ValueError:
        print('Números inválidos. Tente novamente.')
        continue

    op = input('Digite a operação (+, -, *, /): ')
    if op not in op_validas:
        print('Operação inválida. Tente novamente.')
        continue

    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('Divisão por zero não é permitida. Tente novamente.')
            continue
        resultado = num1 / num2

    print(f'O resultado de {num1} {op} {num2} é: {resultado}')
    break
