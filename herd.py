from dinosaur import Dinosaur
dinosaurs = []

class Herd:
    def __init__(self):
        self.herd = ''

    def create_herd(self):
        dino_1 = Dinosaur('T-Rex', 10, 100)
        dinosaurs.append(dino_1)
        dino_2 = Dinosaur('Raptor', 10, 100)
        dinosaurs.append(dino_2)
        dino_3 = Dinosaur('CeraTops', 10, 100)
        dinosaurs.append(dino_3)
        print(dinosaurs)