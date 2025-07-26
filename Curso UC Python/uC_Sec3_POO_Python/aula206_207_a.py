# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json


CAMINHO_ARQUIVO = 'pessoas.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 30)
p2 = Pessoa('Maria', 25)
p3 = Pessoa('José', 40)
pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        print('Fazendo dump...')
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Ele é o main')
    fazer_dump()
    print('Dump feito com sucesso!')