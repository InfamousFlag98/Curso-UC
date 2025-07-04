# reduce - faz a redução de um iterável em um valor

"""
The reduce() function in Python, found within the functools module,
 is a higher-order function that applies a given function cumulatively to the items of an iterable,
 reducing the iterable to a single value.

 from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

output: 15

"""
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))