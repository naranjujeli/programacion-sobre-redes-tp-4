import uuid
import math
from random import randint, random

class Cronopio:

    def __init__(self, pos):

        self.__id == uuid.uuid4()
        self.__life = 100

        self.__pos = pos
        self.__vel = None

        self.__a = self.__random_inicial_value()
        self.__b = self.__random_inicial_value()
        self.__t = self.__random_inicial_value()
        
        self.__t_counter = 0

        self.__d = self.__get_diameter()

    def __new_vel(self):

        p = lambda x: -25*(x**2) + self.__b*x + self.__a
        f = lambda x: 3/(1+(math.e)**(-p(x)))

        x = 2*random() - 1

        return f(x)
    
    def __get_diameter(self):
        
        d = lambda y: max(15 - math.abs(12*y - 3*self.__b), 1)
        y = 2*random() - 1

        return d(y)
    
    def time(self):
        self.__life -= 1
        if self.__t_counter % self.__t == 0:
            self.__change_velocity()
            self.__t_counter = 0
        
    def __change_velocity(self):
        self.__vel = self.__new_vel()

    def eat(self):
        self.__life += 10

    def __random_inicial_value(self):
        return randint(-5, 5)
    
    def calcular_fitness(self):
        pass

    @property
    def id(self):
        return self.__id
    
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def t(self):
        return self.__t
    
    @property
    def life(self):
        return self.__life
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def vel(self):
        return self.__vel
    
    @property
    def diameter(self):
        return self.__d