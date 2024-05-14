class Car:
    price = 1000000

    def horse_powers(self):
        return 'количество лошадиных сил  100'


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return 'количество лошадиных сил  150'


class Kia(Car):
    price = 2000000

    def horse_powers(self):
        return 'количество лошадиных сил  200'


c = Car()
print(c.price)
print(c.horse_powers())
n = Nissan()
print(n.price)
print(n.horse_powers())
k = Kia()
print(k.price)
print(k.horse_powers())




