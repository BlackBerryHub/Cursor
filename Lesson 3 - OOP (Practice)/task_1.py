import random

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Person:
    def __init__(self, name, age, money, has_home):
        self.name = name
        self.age = age
        self.money = money
        self.has_home = has_home

    def info(self):
        print(f"--------- {self.name}'s INFO ----------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money availability: {self.money}")
        print(f"Owns a home: {'Yes' if self.has_home else 'No'}")
        print("----------------------------------")

    def make_money(self, amount):
        self.money += amount

    def buy_home(self, house):
        if self.money > house.cost:
            self.money -= house.cost
            self.has_home = True
            print(f"\n{self.name} successfully buy a house\n")
        else:
            print("You dont have enough money")

class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_discount(self, discount):
        self.cost *= 1 - discount

class Realtor(metaclass=SingletonMeta):

    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def houses_info(self):
        for i, house in enumerate(houses):
            print(f"House #{i} | Area: {house.area} | Price: {house.cost}")

    def give_discount(self, house):
        house.apply_discount(self.discount)

    def sale_house(self, person, house):
        if random.random() < 0.1:
            person.money -= house.cost
            print(f"\nThe realtor stole money from {person.name} :(\n")
        else:
            person.buy_home(house)
            self.houses.remove(house)


if __name__ == "__main__":
    person = Person("Marat", 23, 52500, False)

    houses = [
        House(45, 35000),
        House(50, 40000),
        House(55, 55000)
    ]

    person.info()
    person.make_money(1000)

    r = Realtor("Vasia", houses, 0.1)

    r.give_discount(houses[1])
    r.houses_info()

    r.sale_house(person, houses[1])
    r.houses_info()
    person.info()
