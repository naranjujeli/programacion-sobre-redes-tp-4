from cronopio import Cronopio
from random import randint
from abc import ABC, abstractmethod
from food import Food


class Simulation(ABC):

    def __init__(self, width, height, food_amount, size=21):


        self._width = width
        self._height = height
        
        self._generation_size = size

        self._inicial_cronopios = self.__get_incial_generation()

        self._food = self._get_food(food_amount)
        
    def start(self):
        
        current_generation = self._inicial_cronopios
        while True:
            self.simulate(current_generation)
            current_generation = self.generate()

    def __get_incial_generation(self):
        result = []
        for _ in range(self._generation_size):
            pos_x = randint(0, self._width)
            pos_y = randint(0, self._height)
            new_cronopio = Cronopio((pos_x, pos_y))
            result.append(new_cronopio)
        return result

    def _get_food(self, food_amount):
        result = []
        for _ in range(food_amount):
            pos_x = randint(0, self._width)
            pos_y = randint(0, self._height)
            new_food = Food((pos_x, pos_y))
            result.append(new_food)
        return result

    @abstractmethod
    def simulate(self, generation):
        pass

    def evaluate(self):
        pass

    def generate(self):
        pass

    @property
    def cronopios(self):
        return self._inicial_cronopios

    @property
    def generation_size(self):
        return self._generation_size
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height