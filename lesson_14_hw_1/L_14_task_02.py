import math

class Circle:

    def __init__(self, radius):
        self.radius  = radius



    def dot_intersection(self, dot):
        if math.pow(dot.x, 2) + math.pow(dot.y, 2) <= math.pow(self.radius, 2):
            print ("Точка внутри окружности")
        else: print ("Точка вне окружности")



class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
