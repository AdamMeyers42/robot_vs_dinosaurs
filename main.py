from battlefied import Battlefield

battlefield = Battlefield()
battlefield.run_games()
for dinosaur in battlefield.herd.herd:
    print(dinosaur.name)