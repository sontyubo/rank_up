"""
classmethodの挙動
"""


class Dog:
    species = "犬"  # クラス変数

    def __init__(self, name):
        self.name = name

    def get_species_instance(self):
        return self.species  # インスタンスからアクセス

    @classmethod
    def get_species_class(cls):
        return cls.species  # クラスからアクセス


dog1 = Dog("ポチ")
dog2 = Dog("コロ")

# インスタンスでオーバーライドしてみる
dog1.species = "ネコ"

print(dog1.get_species_instance())  # ネコ ← dog1のインスタンス変数を見てる
print(dog2.get_species_instance())  # 犬   ← クラス変数を見てる

print(Dog.get_species_class())  # 犬   ← クラス全体の値を見てる

# こういう使い方は適切でない #
print(dog1.get_species_class())  # 犬
print(dog2.get_species_class())  # 犬
