from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd= []

    def create_herd(self):
        self.herd.append(Dinosaur('T-Rex', 10, 100))
        self.herd.append(Dinosaur('Raptor', 10, 100))
        self.herd.append(Dinosaur('CeraTops', 10, 100))
        
