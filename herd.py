from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs= []

    def create_herd(self):
        self.dinosaurs.append(Dinosaur('T-Rex', 100, 20))
        self.dinosaurs.append(Dinosaur('Raptor', 100, 15))
        self.dinosaurs.append(Dinosaur('CeraTops', 100, 10))
        
