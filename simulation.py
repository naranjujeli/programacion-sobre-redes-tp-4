from cronopio import Cronopio
from random import randint, choice, random
from abc import ABC, abstractmethod
from food import Food
from vector import Vector


class Simulation(ABC):

    def __init__(self, **kargs):

        self._width = kargs['width']
        self._height = kargs['height']

        self.__food_amount = kargs['food_amount']

        self.__size = Vector(self._width, self._height)
        
        self._generation_size = kargs['size']

        self._frame = kargs['frame']

        self._current_generation = self.__get_incial_generation()

        self._food = self._get_food(self.__food_amount)

        self.__reproduction_pool_size = kargs['reproduction_pool_size']
        
        self._generation_number = 0

        self.__mutation_parameter = kargs['mutation_parameters']

    def set_current_gen(self, new_gen):
        self._current_generation = new_gen
        
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

            new_cronopio = Cronopio(window_size=self.__size, a=new_a, b=new_b, t=new_t, frame=self._frame, d=new_d)
            new_generation.append(new_cronopio)

        self.__mutate(new_generation)
        return new_generation
    
    def __mutate(self, generation):
        
        for cronopio in generation:
            flag = random()
            if flag < self.__mutation_parameter:
                cronopio.mutate()


    def __get_best(self, pool): 
    
        print("---------------")
        sorted_pool = sorted(pool, key=lambda x: x.fitness())
        print(f"avg {self._generation_number}: {sum([i.fitness() for i in sorted_pool])/len(sorted_pool)}")
        result = []
        for i, cronopio in enumerate(sorted_pool[-self.__reproduction_pool_size-1:]):
            result += [cronopio]*i
        print(f"best({self._generation_number}): {max(result, key=lambda x: x.fitness()).fitness()}")
        print("---------------")
        return result


    def __get_incial_generation(self):
        result = []
        for _ in range(self._generation_size):
            a = randint(-1, 1)
            b = randint(-1, 1)
            t = randint(50, 60)
            new_cronopio = Cronopio(window_size=self.__size, a=a, b=b, t=t, frame=self._frame, d=None)
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