from aula206_207_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump
import json

#fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoas_data = json.load(arquivo)
    p1 = Pessoa(**pessoas_data[0])
    p2 = Pessoa(**pessoas_data[1])
    p3 = Pessoa(**pessoas_data[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

