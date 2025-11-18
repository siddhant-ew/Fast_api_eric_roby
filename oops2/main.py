from oops2.enemy import Enemy, zombie, ogre
# print(Enemy.__file__)
# help(Enemy)

# enemy1 = Enemy()
# enemy1.type_of_enemy = "zombie"


enemy = Enemy("zombie",20,2)

enemy.talk()
enemy.walk_forword()
enemy.attack()
# print(f"{enemy.type_of_enemy} has the {enemy.health_points} health points and have attack damage of {enemy.attack_damage}")

zom = zombie(health_points=15, attack_damage=3)
org = ogre(health_point=50, attack_damage=7)
zom.walk_forword()

org.talk()
org.attack()

