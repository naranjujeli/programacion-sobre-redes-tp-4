from simulation import Simulation
import pygame
from vector import Vector

class PygameSimulation(Simulation):

    def __init__(self, **kargs):
        super().__init__(width=kargs['width'], height=kargs['height'],food_amount=kargs['food'], size=kargs['generation_size'], frame=kargs['frame'], reproduction_pool_size=kargs['reproduction_pool_size'], mutation_parameters=kargs['mutation_parameters'])

        self.__size = Vector(kargs['width'], kargs['height'])
        self.__window = self.__get_window(self.__size.get)

        self.__running = False
        self.__new_generation = []
        self._tricker = 0

        
    
    def simulate(self):
        
        self.__x = True
        pygame.display.set_caption(f"Simulacion Evolutiva: {self._generation_number}")
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

        maxsize = 100
        for cronopio in generation:
            red = 255*cronopio.diameter/maxsize
            green = 255*(1-cronopio.diameter/maxsize)
            blue = 255*(1-cronopio.diameter/maxsize)
            if red > 255: red = 255
            if blue > 255: blue = 255
            if green > 255: green = 255
            colors = (red, green, blue)
        
            pygame.draw.circle(self.__window, colors, cronopio.pos, cronopio.diameter)

        for food in self._food:
            pygame.draw.circle(self.__window, (0, 255, 0), food.pos, 3)

        pygame.display.flip()
                    
    def __get_window(self, size):
        return pygame.display.set_mode(size)
        