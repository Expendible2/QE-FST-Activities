class Activity15:
    def __init__(self, manufacture, model, make, transmission, color):
        self.manufacture=manufacture
        self.model=model
        self.make=make
        self.transmission=transmission
        self.color=color
    def accelerate(self):
        print(f"{self.manufacture} {self.model} is moving..")
    def stop(self):
        print(f"{self.manufacture} {self.model} has stopped")
car1=Activity15("BMW",2015,"German","NA","Black")
car2=Activity15("Lambo",2020,"German","NA","Yellow")
car3=Activity15("Maruti",2010,"India","NA","White")
car1.accelerate()
car1.stop()
car2.accelerate()
car2.stop()
car3.accelerate()
car3.stop()