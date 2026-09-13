class Glassware:
    def __init__(self, brand):
        self.brand = brand

class Beaker(Glassware):
    def __init__(self, brand, volume):
        super().__init__(brand)
        self.volume = volume

class Tray:
    def __init__(self, Material):
        self.Material = Material
        self.Beaker_1 = Beaker("Labvida",100)
        self.Beaker_2 = Beaker("Labvida",50)
        self.Beaker_3 = Beaker("Labvida",150)
        self.Beaker_4 = Beaker("Labvida",200)
        self.Beaker_5 = Beaker("Labvida",250)
        print(f"Your {self.Material} tray has been created!")

    def __del__(self):
        print(f"Your {self.Material} tray has been disposed off.")
        del self.Beaker_1
        del self.Beaker_2
        del self.Beaker_3
        del self.Beaker_4
        del self.Beaker_5
        print("All 5 beakers have been disposed off along with the tray.")

my_tray = Tray("Metal")
del my_tray
