class Vehicle:
    def __init__(self, color,engine, breaks):
        self.speed = 0
        self.color = color
        self.engine = engine
        self.breaks = breaks

    def move(self):
        print(f"Машина двигается со скоростью {self.speed}")

    def info(self):
        print(f"Цвет машины {self.color}")
        print(f"Двигатель {self.engine}")
        print(f"Торомоза {self.breaks}")
        

class Car(Vehicle):
    def __init__(self,color,engine, breaks):
        super().__init__(color,engine, breaks)
        self.speed = 100

car = Car("Голубой", 1500, "vip_strong")
car.move()
car.info()