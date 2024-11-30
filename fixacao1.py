# EXERCÍCIO DE FIXAÇÃO 1
# Crie uma classe Televisao (sem acento), em que o usuário é capaz de trocar de canais e aumentar/diminuir o volume. O limite de canais válidos vai de 1 a 15 e o limite de volume válido vai de 0 a 10. No caso de um canal inválido, deve ser definido como padrão o canal 1.

class Televisao:
    def __init__(self):
        self.__canal = 1
        self.__volume = 0
        self.__imprimir()

    def trocar_canal(self, canal):
        if 1 <= canal <= 15:
            self.__canal = canal
        else:
            self.__canal = 1
        self.__imprimir()

    def aumentar_volume(self):
        volume = self.__volume + 1
        self.__volume = volume if volume < 10 else 10
        self.__imprimir()

    def diminuir_volume(self):
        volume = self.__volume - 1
        self.__volume = volume if volume > 0 else 0
        self.__imprimir()

    def __imprimir(self):
        print(f'Televisão - Volume: {self.__volume} | Canal: {self.__canal}')

if __name__ == '__main__':
    tv = Televisao()
    tv.diminuir_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.trocar_canal(13)
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()