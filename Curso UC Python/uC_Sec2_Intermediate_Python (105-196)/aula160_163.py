# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

RESPOSTA SEM CRIAR OUTROS ARQUIVOS
copy, sorted, produtos.sort
Exercícios
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]
Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

novos_produtos = copy.deepcopy(produtos);
for produto in novos_produtos:
produto['preco'] *= 1.10

print(novos_produtos);

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos);

produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda x: x['nome'], reverse= True);
print('\n');
print(produtos_ordenados_por_nome);

produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_nome);

produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda x: x['preco']);
print('\n');
print(produtos_ordenados_por_preco)
"""