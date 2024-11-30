# EXERCÍCIO DE FIXAÇÃO 5
# Crie uma classe Bomba que simule uma bomba de combustíveis de um posto. A bomba pode injetar dois tipos de combustível: gasolina ou álcool, podendo definir no construtor da classe a quantidade e o valor do litro de cada um. Deve possuir os seguintes métodos:
# abastecer_valor(valor, tipo_combustivel), que mostra quantos litros foram colocados no veículo.
# abastecer_litros(litros, tipo_combustivel), que mostra o valor no abastecimento.
# fechar(), que mostra ao final do dia quanto foi ganho no valor total da bomba e quanto sobrou de cada tipo de combustível.

class Bomba:
    def __init__(self, preco_gasolina, preco_alcool):
        self.__preco_gasolina = preco_gasolina
        self.__preco_alcool = preco_alcool
        self.__litros_gasolina = 20000
        self.__litros_alcool = 20000
        self.__valor_total = 0


    def abastecer_valor(self, valor, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            litros = 

