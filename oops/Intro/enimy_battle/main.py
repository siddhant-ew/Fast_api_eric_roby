from oops.Intro.enimy_battle.enemy import Enemy

# enemy1 = Enemy()
# enemy1.type_of_enemy = "zombie"
# print(f"{enemy1.type_of_enemy} has the {enemy1.health_points} health points and have attack damage of {enemy1.attack_damage}")

enemy = Enemy()
enemy.type_of_enemy = "Zombie"

enemy.talk()
enemy.walk_forword()
enemy.attack()