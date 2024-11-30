# EXERCÍCIO DE FIXAÇÃO 5
# Crie uma classe Bomba que simule uma bomba de combustíveis de um posto. A bomba pode injetar dois tipos de combustível: gasolina ou álcool, podendo definir no construtor da classe a quantidade e o valor do litro de cada um. Deve possuir os seguintes métodos:
# abastecer_valor(valor, tipo_combustivel), que mostra quantos litros foram colocados no veículo.
# abastecer_litros(litros, tipo_combustivel), que mostra o valor no abastecimento.
# fechar(), que mostra ao final do dia quanto foi ganho no valor total da bomba e quanto sobrou de cada tipo de combustível.

class Bomba:
    def __init__(self, preco_gasolina, preco_alcool):
        self.__preco_gasolina = preco_gasolina
        self.__preco_alcool = preco_alcool
        self.__tanque_litros_gasolina = 20000
        self.__tanque_litros_alcool = 20000
        self.__faturamento_total = 0

    def abastecer_valor(self, valor, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            litros = valor/self.__preco_gasolina
        elif tipo_combustivel == 'alcool':
            litros = valor/self.__preco_alcool
        self.__armazenamento_tanques(litros, tipo_combustivel)
        self.__atualizar_faturamento(valor)
    
    def abastecer_litros(self, litros, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            valor = litros*self.__preco_gasolina
        elif tipo_combustivel == 'alcool':
            valor = litros*self.__preco_alcool
        self.__armazenamento_tanques(litros, tipo_combustivel)
        self.__atualizar_faturamento(valor)
        
    def __armazenamento_tanques(self, litros, tipo_combustivel):
        if tipo_combustivel == 'gasolina':
            self.__tanque_litros_gasolina -= litros
        elif tipo_combustivel == 'alcool':
            self.__tanque_litros_alcool -= litros
    
    def __atualizar_faturamento(self, faturamento):
        self.__faturamento_total += faturamento

    def fechar(self):
        print(f'Faturamento total no dia: R$ {self.__faturamento_total:.2f}')
        print(f'Tanque de gasolina: {self.__tanque_litros_gasolina:.1f} litros')
        print(f'Tanque de álcool: {self.__tanque_litros_alcool:.1f} litros')

bomba = Bomba(6, 5)
bomba.abastecer_litros(25, 'gasolina')
bomba.abastecer_valor(100, 'alcool')
bomba.fechar()
