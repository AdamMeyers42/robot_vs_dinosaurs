from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []
    
    def create_fleet(self):
        robot_1 = Robot('bobby_robot', 100, 'Sword')
        self.fleet.append(robot_1)
        robot_2 = Robot('dean_robot', 100, 'Sword')
        self.fleet.append(robot_2)
        robot_3 = Robot('sam_robot', 100, 'Sword')
        self.fleet.append(robot_3)

