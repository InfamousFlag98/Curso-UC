# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    def apresentar(self):
        return f'Carro: {self.nome}, Motor: {self.motor.nome if self.motor else "Nenhum"}, Fabricante: {self.fabricante.nome if self.fabricante else "Nenhum"}'

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

polo = Carro('Polo')
motor_1_0_turbo = Motor('1.0 Turbo TSI')
volks = Fabricante('Volkswagen')
polo.motor = motor_1_0_turbo
polo.fabricante = volks

mobi = Carro('Mobi')
motor_1_0_aspirado = Motor('1.0 Aspirado')
fiat = Fabricante('Fiat')
mobi.motor = motor_1_0_aspirado
mobi.fabricante = fiat

gol = Carro('Gol')
motor_1_6 = Motor('1.6 MSI')
gol.motor = motor_1_6
gol.fabricante = volks

fox = Carro('Fox')
fox.motor = motor_1_0_aspirado
fox.fabricante = volks

apresentacoes = [polo.apresentar(), mobi.apresentar(), gol.apresentar(), fox.apresentar()]
for apresentacao in apresentacoes:
    print(apresentacao)