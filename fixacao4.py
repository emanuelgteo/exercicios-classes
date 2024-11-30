# EXERCÍCIO DE FIXAÇÃO 4
# Crie uma classe Carro com as seguintes funcionalidades:
# Um veículo tem certo consumo de combustível (medido em km/l) e certa quantidade de combustível no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método abastecer(), que abasteça o carro com o valor passado de litros de combustível.
# Forneça um método andar(), que simule o ato de dirigir o veículo por certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método nivel_combustivel(), que retorne o nível atual de combustível.

class Carro:
    def __init__(self, consumo):
        self.__consumo = consumo
        self.__combustivel = 0
        self.nivel_combustivel()

    def abastecer(self, litros):
        self.__combustivel += litros
        self.nivel_combustivel()
    
    def andar(self, distancia):
        distancia_possivel = self.__combustivel*self.__consumo
        if distancia > distancia_possivel:
            print(f'Distância muito longa. O carro andou {distancia_possivel:.1f} km')
            self.__combustivel = 0
        else:
            self.__combustivel -= distancia/self.__consumo
        self.nivel_combustivel()

    def nivel_combustivel(self):
        print(f'Nível de combustível: {self.__combustivel:.1f} litros')

carro = Carro(13)
carro.abastecer(55)
carro.andar(500)
carro.abastecer(10)
carro.andar(500)