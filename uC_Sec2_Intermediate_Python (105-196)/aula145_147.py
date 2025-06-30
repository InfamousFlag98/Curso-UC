import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
dgenerator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(dgenerator))

print(dgenerator)

# for n in generator:
#     print(n)


# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n, maximum):
    while True:
        yield n
        n += 1
        print("Continuando...")

        if n >= maximum:
            print("Fim da execução")
            return


gen = generator(n=1, maximum=1000000)
for n in gen:
    print(n)