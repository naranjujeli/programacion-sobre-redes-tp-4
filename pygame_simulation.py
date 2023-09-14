from simulation import Simulation
import pygame

class PygameSimulation(Simulation):

    def __init__(self, width, height, generation_size=21):
        super().__init__(width, height, generation_size)

        self.__window = self.__get_window((width, height))
    
    def simulate(self, generation):
        
        pygame.init()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for cronopio in generation:
                cronopio.time()
                for food in self._food:
                    if cronopio.able_to_eat(food):
                        cronopio.eat()
                        self._food.remove(food)

            #self.__window.fill((0, 0, 0))

            for cronopio in generation:
                pygame.draw.circle(self.__window, (0, 120, 120), cronopio.pos, cronopio.r)

            for food in self._food:
                pygame.draw.cirlce(self.__window, (0, 255, 0), food.pos, 3)
                    

            
                
            

    def __get_window(self, size):
        return pygame.display.set_mode(size)
        