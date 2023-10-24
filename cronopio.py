import uuid
import math
from random import randint, random, choice
from vector import Vector

class Cronopio:

    def __init__(self, **kargs):

        self.__id = uuid.uuid4()
        self.__inicial_life_duration = 1000
        self.__life = self.__inicial_life_duration

        self.__duration = 0

        self.__frame = kargs['frame']

        pos_x = randint(self.__frame, kargs['window_size'].x - self.__frame)
        pos_y = randint(self.__frame, kargs['window_size'].y - self.__frame)
        self.__pos = Vector(pos_x, pos_y)

        self.__a = kargs['a']
        self.__b = kargs['b']
        self.__t = kargs['t']

        self.__vel = self.__new_vel()
        
        self.__t_counter = 0

        if not kargs['d']:
            self.__d = self.__get_diameter()
        else:
            self.__d = kargs['d']

        self.__alive = True

    def __eq__(self, other):
        return self.__id == other.id

    def fitness(self):
        return self.__duration
    
    def mutate(self):
        
        self.__a = randint(-1, 1)
        self.__b = randint(-1, 1)
        self.__t += choice([-5, 5])
        self.__d += 2

    def time(self, window_size):

        self.__life -= 1
        self.__duration += 1
        if self.__life == 0:
            self.__alive = False
            return
        self.__t_counter += 1
        if self.__t_counter % self.__t == 0:
            self.__t_counter = 0
            self.__update(window_size)   
        self.__move()

    def __update(self, window_size):
        self.__change_velocity()
        self.__update_movement()
        self.__bounce(window_size)

    def __change_velocity(self):
        self.__vel = self.__new_vel()
    
    def __new_vel(self):

        p = lambda x: -25*(x**2) + self.__b*x + self.__a
        f = lambda x: 3/(1+(math.e)**(-p(x)))
        x = 2*random() - 1

        new_vel_mag = f(x)
        new_vel = Vector(1, 1)
        new_vel.set_mag(new_vel_mag)
        return new_vel
    
    def __update_movement(self):
        angle = randint(-5, 5)
        self.__vel.change_dir(angle)

    def __bounce(self, window_size):

        if self.__pos.x + self.__d > window_size.x: self.__pos.set_x(self.__frame)
        if self.__pos.x - self.__d < 0: self.__pos.set_x(window_size.x-self.__frame)
        if self.__pos.y + self.__d > window_size.y: self.__pos.set_y(self.__frame)
        if self.__pos.y - self.__d < 0: self.__pos.set_y(window_size.y-self.__frame)

    def __move(self):
        self.__pos += self.__vel

    def eat(self):
        self.__life += self.__inicial_life_duration/10

    def able_to_eat(self, food):
        
        dif_x = abs(food.x - self.__pos.x)
        dif_y = abs(food.y - self.__pos.y)
        distance = math.sqrt(dif_x**2 + dif_y**2)

        return distance < (self.__d)
    
    def __get_diameter(self):
        
        d = lambda y: max(15 - abs(12*y - 3*self.__b), 1)
        y = 2*random() - 1

        return d(y)*1
    
    @property
    def alive(self):
        return self.__alive
    
    @property
    def duration(self):
        return self.__duration

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
        return (self.__pos.x, self.__pos.y)
    
    @property
    def vel(self):
        return self.__vel
    
    @property
    def diameter(self):
        return self.__d

    @property
    def frame(self):
        return self.__frame
    

class ParserCronopio:

    def __init__(self): pass

    def from_cronopio_to_json(self, cronopio):
        
        return {
                "diameter": cronopio.diameter,
                "duration": cronopio.duration,
                "a": cronopio.a,
                "b": cronopio.b,
                "t": cronopio.t,
                "id": cronopio.id
        }
    
    def from_json_to_cronopio(self, cronopio_json):
        identifier = [key for i, key in enumerate(cronopio_json.keys()) if i == 0][0]
        frame = cronopio_json[identifier]['frame']
        a = cronopio_json[identifier]['a']
        b = cronopio_json[identifier]['b']
        t = cronopio_json[identifier]['t']
        d = cronopio_json[identifier]['d']  
        return Cronopio(a= a, b= b, t= t, d= d, frame= frame, window_size = Vector(0, 0))