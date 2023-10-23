import math

class Vector:

    def __init__(self, x, y):

        self.__x = x
        self.__y = y

        self.__mag = self.__get_mag()

    def __iadd__(self, other):

        return Vector(self.__x + other.x, self.__y + other.y)

    @property
    def get(self):
        return (self.__x, self.__y)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def mag(self):
        return self.__mag
    
    def set_dir(self, dir):
        
        x = self.__get_mag()*math.cos(dir)
        y = self.__get_mag()*math.sin(dir)

        self.set([x, y])

    def normalize(self):

        dir = self.get_dir()
        new_vector = Vector(1, 1)
        new_vector.set_dir(dir)
        return new_vector
    
    def scale(self, s):

        self.__x *= s
        self.__y *= s

    def set_mag(self, new_mag):
        
        dir = self.get_dir()
        self.set_dir(dir)
        self.scale(new_mag)
        

    def change_dir(self, off):

        self.set_dir(self.get_dir() + off)
    
    def get_dir(self, mode="DEGRESS"):

        if mode == "DEGRESS":
            return math.atan(self.__y / self.__x)
        elif mode == "RADIANS":
            return math.atan(self.__y / self.__x) * math.pi/180
    
    def __get_mag(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def set(self, new):

        self.__x = new[0]
        self.__y = new[1]