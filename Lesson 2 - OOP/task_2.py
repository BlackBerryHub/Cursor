"""
1.a. Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    Human class, should have eat, sleep, study, work

class Centaur(.. , ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""

class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating as human")

    def sleep(self):
        print(f"{self.name} is sleeping as human")

    def studying(self):
        print(f"{self.name} is studying as human")

    def work(self):
        print(f"{self.name} is working as human")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating as animal")

    def sleep(self):
        print(f"{self.name} is sleeping as animal")


class Centaur(Human, Animal):
    def __init__(self, name):
        super().__init__(name)
        Animal.__init__(self, name)

    def eat_as_centaur(self):
        print(f"{self.name} is eating as centaur")

    def eat_as_human(self):
        super().eat()

    def eat_as_animal(self):
        Animal.eat(self)


centaur = Centaur("Vasia")

centaur.eat_as_centaur()
centaur.eat_as_animal()
centaur.eat_as_human()
