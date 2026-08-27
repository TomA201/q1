class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, damagetaken):
        self.hp = self.hp - damagetaken
        print("Your hero,",self.name, "has taken", damagetaken, "damage!")
        print(self.name, "has", self.hp, "hp left.")

Hero1 = Hero("Arthur", 100)
Hero2 = Hero("Morgana", 100)
damagetakennyaruthur = 10
Hero1.take_damage(damagetakennyaruthur)
print(Hero1.name,"'s hp is",Hero1.hp)
print(Hero2.name,"'s hp is",Hero2.hp)
