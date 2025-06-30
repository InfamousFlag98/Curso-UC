import os
import time
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
def exibir_perguntas(perguntas):
    qtd_acertos = 0
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        for i, opcao in enumerate(pergunta['Opções'], start=1):
            print(f"opção {i}: {opcao}.")
        while True:
            resposta_usuario = input("Digite o número da sua resposta: ")
            if resposta_usuario.isdigit():
                idx = int(resposta_usuario) - 1
                if 0 <= idx < len(pergunta['Opções']):
                    break
            print("Entrada inválida. Tente novamente.")
        if pergunta['Opções'][idx] == pergunta['Resposta']:
            print("Resposta correta!\n")
            time.sleep(3)
            os.system('cls')
            qtd_acertos += 1
        else:
            print(f"Resposta incorreta! A resposta correta é: opção{i}. {pergunta['Resposta']}\n")
            time.sleep(3)
        os.system('cls')
    return qtd_acertos

print("Bem-vindo ao Quiz!")
acertos = exibir_perguntas(perguntas)
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
print("Obrigado por jogar!")
time.sleep(3)
os.system('cls')
# Fim do Quiz