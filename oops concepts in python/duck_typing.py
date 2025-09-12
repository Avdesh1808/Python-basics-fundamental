# this is the example of duck typing 
class car:
    def drive(self):
        print("car can start !")
class boat:
    def drive(self):
        print("boat can sailing !")
class bike:
    def drive(self):
        print("bike can start !")
class airoplan:
    def fly(self):
        print("airplane can fly !") # but this giva an error beacuse has not drive method
    
def start_engine(vehicle):
    vehicle.drive()
start_engine(car())
start_engine(boat())
start_engine(bike())
#start_engine(airoplan())
