from cronopio import Cronopio
from random import randint
from abc import ABC, abstractmethod


class Simulacion(ABC):

    def __init__(self, ancho, alto, tamanio_por_generacion=21):


        self.__alto = alto
        self.__ancho = ancho
        
        self.__tamanio_por_generacion = tamanio_por_generacion

        self.__cronopios = []
        for _ in range(1, self.__tamanio_por_generacion + 1):
            pos_x = randint(0, self.__ancho)
            pos_y = randint(0, self.__alto)
            nuevo_cronopio = Cronopio((pos_x, pos_y))
            self.__cronopios.append(nuevo_cronopio)

    @abstractmethod
    def simular(self):
        pass

    def evualar(self):
        pass

    def generar(self):
        pass

    @property
    def cronopios(self):
        return self.__cronopios
    
    @property
    def tamanio(self):
        return self.__tamanio_por_generacion