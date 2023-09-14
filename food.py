

class Food:

    def __init__(self, pos):

        self.__pos = pos

    @property
    def pos(self):
        return self.__pos
    
    @property
    def x(self):
        return self.__pos[0]
    
    @property
    def y(self):
        return self.__pos[1]