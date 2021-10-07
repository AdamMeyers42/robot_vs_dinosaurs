from battlefied import Battlefield

battlefield = Battlefield()
battlefield.run_games()
for dinosaur in battlefield.herd.dinosaurs:
    print(dinosaur.name)

for robot in battlefield.fleet.robots:
    print(robot.name)