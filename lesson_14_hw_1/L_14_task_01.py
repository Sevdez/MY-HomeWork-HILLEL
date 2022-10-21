class Godzilla ():

    def __init__(self):
        self.belly_size = 1000
        self.filled_size = 0

    def eat (self, human_weight):
        if self.filled_size >= self.belly_size * 0.9:
            print ("I`m full")
        else: self.filled_size += human_weight