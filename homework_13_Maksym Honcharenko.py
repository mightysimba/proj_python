#magicmethod

class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, newcountry):
        newname = self.name + " " + newcountry.name
        newpopulation = self.population + newcountry.population
        return Country(newname, newpopulation)


bosnia = Country('Bosnia', 10_000_000)

herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


#create a Car class
class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        return self.speed + 5

    def brake(self):
        newspeed = self.speed - 5
        if newspeed < 0:
            max(0, newspeed)

    def display_speed(self):
        print("your current speed is: " + self.speed)


toyota = Car("Toyota", "yaris", 2002, 1)
print(toyota.accelerate())
print(toyota.brake())
