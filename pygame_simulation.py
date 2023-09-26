from simulation import Simulation
import pygame
from vector import Vector

class PygameSimulation(Simulation):

    def __init__(self, width, height, food_amount, generation_size=21):
        super().__init__(width, height,food_amount, generation_size)

        self.__size = Vector(width, height)
        self.__window = self.__get_window(self.__size.get)
        pygame.display.set_caption("Simulacion Evolutiva")

        self.__running = False
        self.__new_generation = []
    
    def simulate(self):
        
        pygame.init()

        self.__running = True
        while self.__running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            if self.__update(self._current_generation): return self.__new_generation

    def __update(self, generacion):
        if self.__update_cronopios(generacion): return True
        self.__update_window(generacion)

    def __update_cronopios(self, generation): 
        for cronopio in generation:
            cronopio.time(self.__size)
            for food in self._food:
                if cronopio.able_to_eat(food):
                    cronopio.eat()
                    self._food.remove(food)
            if not cronopio.alive: 
                self.__new_generation.append(cronopio)
                generation.remove(cronopio)
            if len(generation) == 0:
                return True
        return False

    def __update_window(self, generation):
        self.__window.fill((0, 0, 0))

        for cronopio in generation:
            pygame.draw.circle(self.__window, (0, 120, 120), cronopio.pos, cronopio.diameter)

        for food in self._food:
            pygame.draw.circle(self.__window, (0, 255, 0), food.pos, 3)

        pygame.display.flip()
                    
    def __get_window(self, size):
        return pygame.display.set_mode(size)
        