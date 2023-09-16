from simulation import Simulation
import pygame
from vector import Vector

class PygameSimulation(Simulation):

    def __init__(self, width, height, food_amount, generation_size=21):
        super().__init__(width, height,food_amount, generation_size)

        self.__size = Vector(width, height)
        self.__window = self.__get_window(self.__size.get)
        pygame.display.set_caption("Simulacion Evolutiva")

        self.__generations = []
    
    def simulate(self, generation):
        
        pygame.init()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__update(generation)
        
    def __update(self, generation):
        self.__update_cronopios(generation)
        self.__update_window(generation)

    def __update_cronopios(self, generation): 
        for cronopio in generation:
            cronopio.time(self.__size)
            for food in self._food:
                if cronopio.able_to_eat(food):
                    cronopio.eat()
                    self._food.remove(food)
            if cronopio.life <= 0:
                generation.remove(cronopio)

    def __update_window(self, generation):
        self.__window.fill((0, 0, 0))

        for cronopio in generation:
            pygame.draw.circle(self.__window, (0, 120, 120), cronopio.pos, cronopio.diameter)

        for food in self._food:
            pygame.draw.circle(self.__window, (0, 255, 0), food.pos, 3)

        pygame.display.flip()
                    
    def __get_window(self, size):
        return pygame.display.set_mode(size)
        