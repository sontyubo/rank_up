"""
classmethodの応用1
サブクラスに応じた柔軟なインスタンス生成（継承対応）
"""


class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)


class Cat(Animal):
    def speak(self):
        return print(f"{self.name} say meow!")


class Bird(Animal):
    def speak(self):
        return print(f"{self.name} say tweet!")


M = Cat.create("Mike")
S = Bird.create("Sam")

M.speak()
S.speak()
