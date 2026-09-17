class TusokTusok:
  name = ""
  def __init__(self,name):
    self.name = name
  def dip(self,sauce):
    self.sauce = sauce
  def eat(self):
    print("I ate",self.name,"with",self.sauce.name,"and it tasted",self.sauce.taste)
class Sauce:
  name = ""
  taste = ""
  def __init__(self,name,taste):
    self.name = name
    self.taste = taste

fishball = TusokTusok("fishball")
vinegar = Sauce("vinegar","sour")
fishball.dip(vinegar)
fishball.eat()
