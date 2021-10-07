from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        herd = Herd()
        herd.create_herd()
        self.herd = herd

        fleet = Fleet()
        fleet.create_fleet()
        self.fleet = fleet

    def run_games(self):
        self.display_welcome()

    def display_welcome(self):
        print('Welcome to the ThunderDome! \n')
        print('Here are your contestants! \n')
        print('Here are your dinosaurs! \n')
        for dinosaur in self.herd.dinosaurs:
            print(f'{dinosaur.name}: hp - {dinosaur.health} ap - {dinosaur.attack_power}')

        print('\nHere are your robots! \n')
        for robot in self.fleet.robots:
            print(f'{robot.name}: hp - {robot.health} ap - {robot.weapon.attack_power}')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        dinosaur.attack(random.choice(self.fleet.robots))
    
    def robo_turn(self, robot):
        robot.attack(random.choice(self.herd.dinosaurs))

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
