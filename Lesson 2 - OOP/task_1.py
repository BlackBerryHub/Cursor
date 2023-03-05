"""
1. Сreate a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class

class Animals:
Parent class, should have eat, sleep

class Animal1(Animal):
Some of the animal with 1-2 extra methods related to this animal
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Cat(Animal):
    def meaw(self):
        print(f"{self.name} is meawing")

    def catch_mouse(self) :
        print(f"{self.name} catching a mouse")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Parrot(Animal):
    def repeat(self):
        print(f"{self.name} is repeating")


class Monkey(Animal):
    def eat_banana(self):
        print(f"{self.name} is eating banana")


class Snake(Animal):
    def crawling(self):
        print(f"{self.name} is crawling")


if __name__ == "__main__" :
    cat = Cat("Vasia")
    dog = Dog("Patron")
    parrot = Parrot("Grisha")
    monkey = Monkey("Mawpik")
    snake = Snake("Zmiya")

    cat.sleep()
    cat.meaw()
    dog.bark()
    parrot.repeat()
    monkey.eat_banana()
    snake.crawling()

    print(f"Check if {cat.name} is instance of Animal: {isinstance(cat, Animal)}")
    print(f"Check if {dog.name} is instance of Animal: {isinstance(dog, Animal)}")
    print(f"Check if {parrot.name} is instance of Animal: {isinstance(parrot, Animal)}")
    print(f"Check if {monkey.name} is instance of Animal: {isinstance(monkey, Animal)}")
    print(f"Check if {snake.name} is instance of Animal: {isinstance(snake, Animal)}")
