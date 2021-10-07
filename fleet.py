from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robots.append(Robot('bobby_robot', 100, 'Sword'))
        self.robots.append(Robot('dean_robot', 100, 'Sword'))
        self.robots.append(Robot('sam_robot', 100, 'Sword'))
        
       