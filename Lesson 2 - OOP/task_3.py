from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass

class HPLaptop(Laptop):

    def screen(self):
        print("This is HP Laptop Screen method")

    def keyboard(self):
        print("This is HP Laptop Keyboard method")

    def touchpad(self):
        print("This is HP Laptop Touchpad method")

    def webcam(self):
        print("This is HP Laptop Webcam method")

    def ports(self):
        print("This is HP Laptop Ports method")

    def dynamics(self):
        print("This is HP Laptop Dynamics method")

if __name__ == "__main__":

    hp_laptop = HPLaptop()

    hp_laptop.screen()
    hp_laptop.keyboard()
    hp_laptop.touchpad()
    hp_laptop.webcam()
    hp_laptop.ports()
    hp_laptop.dynamics()
