# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

print(string)

#print(dir(string))  # Mostra os métodos e atributos do objeto string

if hasattr(string, metodo):
    print(f'A string tem o método {metodo}')
    print(getattr(string, metodo)())  # Chama o método upper da string
else:
    print(f'A string não tem o método {metodo}')