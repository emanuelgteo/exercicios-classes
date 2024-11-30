# EXERCÍCIO DE FIXAÇÃO 2
# Crie uma classe de cartas de baralho com o nome de Carta. Ao imprimir a carta, deve ser mostrada uma carta de 1 a 10 ou figuras (dama, valete ou rei) e um naipe (ouros, espadas, copas ou paus).
import random

class Carta:
    
    naipes = ['ouros', 'espadas', 'copas', 'paus']
    cartas = ['ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valete', 'dama', 'rei']

    def __init__(self):
        self.__carta = random.choice(Carta.cartas)
        self.__naipe = random.choice(Carta.naipes)
        self.imprimir()

    def imprimir(self):
        print(f'{self.__carta} de {self.__naipe}')

for i in range(5):
    Carta()