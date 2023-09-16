import uuid
import math
from random import randint, random, choice
from vector import Vector

class Cronopio:

    def __init__(self, pos):

        self.__id = uuid.uuid4()
        self.__life = 100

        self.__pos = Vector(pos[0], pos[1])

        self.__a = self.__random_inicial_value()
        self.__b = self.__random_inicial_value()
        self.__t = randint(50, 60)

        self.__vel = self.__new_vel()
        
        self.__t_counter = 0

        self.__d = self.__get_diameter()

    def __new_vel(self):

        p = lambda x: -25*(x**2) + self.__b*x + self.__a
        f = lambda x: 3/(1+(math.e)**(-p(x)))

        x = 2*random() - 1

        new_vel = Vector(1, 1)
        new_vel.set_mag(f(x))
        return new_vel
    
    def __get_diameter(self):
        
        d = lambda y: max(15 - abs(12*y - 3*self.__b), 1)
        y = 2*random() - 1

        return d(y)
    
    def time(self, window_size):
        self.__life -= 1
        self.__t_counter += 1
        if self.__t_counter % self.__t == 0:
            self.__t_counter = 0
            self.__change_velocity()
            self.__update_movement()
            self.__bounce(window_size)
        self.__move()

    def __move(self):

        self.__pos += self.__vel

    def __bounce(self, window_size):

        r = self.__d/2

        if self.__pos.x + r > window_size.x or self.__pos.x - r < 0:
            self.__vel *= -1
        if self.__pos.y + r > window_size.y or self.__pos.y - r < 0:
            self.__vel *= -1
    
    def __update_movement(self):
        
        angle = random(360)
        self.__vel.set_dir(angle)
        
    def __change_velocity(self):
        self.__vel = self.__new_vel()

    def eat(self):
        self.__life += 10

    def __random_inicial_value(self):
        return randint(-5, 5)
    
    def fitness(self):
        pass

    def able_to_eat(self, food):
        
        print(type(food))
        print(type(self.__pos))

        dif_x = abs(food.x - self.__pos.x)
        dif_y = abs(food.y - self.__pos.y)

        distance = math.sqrt(dif_x**2 + dif_y**2)

        return distance < (self.__d/2)

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