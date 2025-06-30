# nos caminhos de sys.path

import aula154_m
from aula154_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula154_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula154_m.soma(2, 3))

from sys import path

import uMY_SPOTIFY_APPS.modulo
from uMY_SPOTIFY_APPS import modulo
from uMY_SPOTIFY_APPS.modulo import *

# from uMY_SPOTIFY_APPS
#.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(uMY_SPOTIFY_APPS.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)