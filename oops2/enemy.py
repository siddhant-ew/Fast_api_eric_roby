class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def __init__(self,type_of_enemy,health_points=10,attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}, be prepared to fight!")

    def walk_forword(self):
        print(f"The {self.type_of_enemy} is walking forword")

    def attack(self):
        print(f"The {self.type_of_enemy} is attacking with {self.attack_damage} damage")

class zombie(Enemy):

    def __init__(self, health_points, attack_damage):
    
        super().__init__(type_of_enemy="zombie",health_points=health_points,attack_damage=attack_damage)
        
    def talk(self):
        return "Grumbling!!!"
    
    def spread_disease(self):
        return "Bite and spread the disease"
    
class ogre(Enemy):

    def __init__(self, health_point, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_point, attack_damage=attack_damage)

    def attack(self):
        return "run and spit slime!! yakk"

