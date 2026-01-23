#Create a Car class with attributes like make, model, year, and a method display_car_info that prints all the information of the car.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_car_info(self):
        print("Car Information:")
        print(f"  Make  : {self.make}")
        print(f"  Model : {self.model}")
        print(f"  Year  : {self.year}")
        print("-" * 30)
car1 = Car("Toyota", "Innova Crysta", 2023)
car1.display_car_info()
car2 = Car("Tesla", "Model Y", 2025)
car2.display_car_info()

'''output:
Car Information:
  Make  : Toyota
  Model : Innova Crysta
  Year  : 2023
------------------------------
Car Information:
  Make  : Tesla
  Model : Model Y
  Year  : 2025
------------------------------'''
