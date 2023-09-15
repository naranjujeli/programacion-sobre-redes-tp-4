import math

class Vector:

    def __init__(self, x, y):

        self.__x = x
        self.__y = y

        self.__mag = self.__get_mag()

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def mag(self):
        return self.__mag
    
    def get_dir(self, mode="DEGRESS"):

        if mode == "DEGRESS":
            return math.arctan(self.__y / self.__x)
        elif mode == "RADIANS":
            pass
    
    def __get_mag(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def set(self, new):

        self.__x = new[0]
        self.__y = new[1]