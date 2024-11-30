# EXERCÍCIO DE FIXAÇÃO 3
# Crie uma classe Baralho que possua um vetor com cada uma das cartas do baralho. A classe deve possuir um método sortear, que retorne uma das cartas. Essa carta não pode mais ser retornada. O baralho deve possuir, ainda, dois coringas. Ao retornar todas as 54 cartas, deve informar que as cartas acabaram.

import random

class Baralho:

    def __init__(self):
        self.__gerar_baralho()
        self.__embaralhar()

    def __gerar_baralho(self):
        valor_cartas = list(range(1,11)) + ['valete', 'dama', 'rei']
        naipes = ['ouros', 'copas', 'espadas', 'paus']
        self.__cartas = ['coringa', 'coringa']

        for valor in valor_cartas:
            for naipe in naipes:
                carta = f'{valor} de {naipe}'
                self.__cartas.append(carta)
    
    def __embaralhar(self):
        random.shuffle(self.__cartas)

    def sortear(self):
        carta_sorteada = self.__cartas.pop()
        print(f'Carta sorteada: {carta_sorteada}')
        self.__quantidade_cartas()
    
    def __quantidade_cartas(self):
        quantidade = len(self.__cartas)
        if quantidade < 0:
            print(f'As cartas do baralho acabaram')
        elif quantidade == 1:
            print(f'Resta {quantidade} carta no baralho.')
        else:
            print(f'Restam {quantidade} cartas no baralho.')

baralho = Baralho()

for i in range(54):
    baralho.sortear()