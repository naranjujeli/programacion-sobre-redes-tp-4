from simulation import Simulation
import pygame
from vector import Vector

class PygameSimulation(Simulation):

    def __init__(self, width, height, food_amount, generation_size=21):
        super().__init__(width, height,food_amount, generation_size)

        self.__size = Vector(width, height)
        self.__window = self.__get_window(self.__size.get)
        pygame.display.set_caption("Simulacion Evolutiva")
    
    def simulate(self, generation):
        
        pygame.init()

        running = True
        counter = 0
        while running:

            #print(counter)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for cronopio in generation:
                cronopio.time(self.__size)
                for food in self._food:
                    if cronopio.able_to_eat(food):
                        cronopio.eat()
                        self._food.remove(food)

            self.__window.fill((0, 0, 0))

            for cronopio in generation:
                pygame.draw.circle(self.__window, (0, 120, 120), cronopio.pos, cronopio.diameter)

            for food in self._food:
                pygame.draw.circle(self.__window, (0, 255, 0), food.pos, 3)

            pygame.display.flip()

            counter += 1
            if counter == 100:
                #break
                pass
                    
    def __get_window(self, size):
        return pygame.display.set_mode(size)
        