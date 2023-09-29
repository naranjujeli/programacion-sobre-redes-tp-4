from cronopio import Cronopio
from random import randint, choice, random
from abc import ABC, abstractmethod
from food import Food
from vector import Vector


class Simulation(ABC):

    def __init__(self, width, height, food_amount, size=21):

        self._width = width
        self._height = height

        self.__food_amount = food_amount

        self.__size = Vector(self._width, self._height)
        
        self._generation_size = size

        self._frame = 15

        self._current_generation = self.__get_incial_generation()

        self._food = self._get_food(self.__food_amount)

        self.__reproduction_pool_size = 7
        
        self._generation_number = 0

        self.__mutation_parameter = 0.4
        
    def cicle(self):
        self._generation_number += 1
        
        dead_generation = self.simulate()
        self._food = self._get_food(self.__food_amount)
        self._current_generation = self.generate(dead_generation)

    def generate(self, generacion): 

        new_generation = []
        #print(f"generacion: {len(generacion)}")
        winners = self.__get_best(generacion)
        while len(new_generation) <= self._generation_size:
            parent1 = choice(winners)
            parent2 = choice(winners)
            new_a = (parent1.a + parent2.a)/2
            new_b = (parent1.b + parent2.b)/2
            new_t = (parent1.t + parent2.t)/2
            new_d = (parent1.diameter + parent2.diameter)/2

            new_cronopio = Cronopio(self.__size, new_a, new_b, new_t, self._frame, new_d)
            new_generation.append(new_cronopio)

        self.__mutate(new_generation)
        return new_generation
    
    def __mutate(self, generation):
        
        for cronopio in generation:
            flag = random()
            if flag < self.__mutation_parameter:
                cronopio.mutate()


    def __get_best(self, pool): 
    
        #print(f"pool: {pool}")
        result = sorted(pool, reverse=True, key=lambda x: x.fitness())
        print(f"best({self._generation_number}): ", result[0].fitness())
        return result[:self.__reproduction_pool_size]


    def __get_incial_generation(self):
        result = []
        for _ in range(self._generation_size):
            a = randint(-1, 1)
            b = randint(-1, 1)
            t = randint(50, 60)
            new_cronopio = Cronopio(self.__size, a, b, t, self._frame)
            result.append(new_cronopio)
        return result

    def _get_food(self, food_amount):
        result = []
        for _ in range(food_amount):
            pos_x = randint(0, self._width)
            pos_y = randint(0, self._height)
            new_food = Food([pos_x, pos_y])
            result.append(new_food)
        return result

    @abstractmethod
    def simulate(self, generation):
        pass

    def _add_to_reproduction_pool(self, cronopio):
        self._reproduction_pool.append(cronopio)

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