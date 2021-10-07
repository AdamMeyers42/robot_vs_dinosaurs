from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robots.append(Robot('bobby', 100, Weapon('Sword', 10)))
        self.robots.append(Robot('dean', 100, Weapon('Laser Rifle', 15)))
        self.robots.append(Robot('sam', 100, Weapon('Ion Cannon', 20)))
        
       