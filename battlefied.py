from dinosaur import Dinosaur
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
        while (len(self.fleet.robots) > 0) and (len(self.herd.dinosaurs) > 0):
            self.robo_turn(random.choice(self.fleet.robots))
            self.dino_turn(random.choice(self.herd.dinosaurs))

        self.display_winners()

    def display_welcome(self):
        print('Welcome to the ThunderDome! \n')
        print('Here are your contestants! \n')
        print('Dino Team! \n')
        for dinosaur in self.herd.dinosaurs:
            print(
                f'{dinosaur.name}: hp - {dinosaur.health} ap - {dinosaur.attack_power}')

        print('\nRobo Team! \n')
        for robot in self.fleet.robots:
            print(
                f'{robot.name}: hp - {robot.health} ap - {robot.weapon.attack_power}')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        robot = random.choice(self.fleet.robots)
        dinosaur.attack(robot)
        print(f'{dinosaur.name} attacked {robot.name} for {dinosaur.attack_power}!')
        print(f'{robot.name}\'s life is now at {robot.health}')
        if robot.health <= 0:
            print('He dead')
            self.fleet.robots.remove(robot)
            print('Here are your remaining robots! \n')
            for robot in self.fleet.robots:
                 print(
                    f'{robot.name}: hp - {robot.health} ap - {robot.weapon.attack_power}')


    def robo_turn(self, robot):
        dinosaur = random.choice(self.herd.dinosaurs)
        robot.attack(dinosaur)
        print(f'{robot.name} attacked {dinosaur.name} with {robot.weapon.name} for {robot.weapon.attack_power}!')
        print(f'{dinosaur.name}\'s life is now at {dinosaur.health}')
        if dinosaur.health <= 0:
            print('He dead')
            self.herd.dinosaurs.remove(dinosaur)
            print('Here are your remaining dinosaurs! \n')
            for dinosaur in self.herd.dinosaurs:
                print(
                    f'{dinosaur.name}: hp - {dinosaur.health} ap - {dinosaur.attack_power}')

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
