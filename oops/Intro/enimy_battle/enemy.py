class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}, be prepared to fight!")

    def walk_forword(self):
        print(f"The {self.type_of_enemy} is walking forword")

    def attack(self):
        print(f"The {self.type_of_enemy} is attacking with {self.attack_damage} damage")
        

