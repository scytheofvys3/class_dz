from random import randint

class  Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz < 0:
            print('Слишком глубоко, я не могу нырнуть')
            return
        else:
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print(f'Острожно, я тебя атакую 0_0')
        else:
            print(f'Извините, я мирный')


    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        ran1_4 = randint(1, 4)
        print(f'Вот (есть) {ran1_4} яйца для тебя')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz
        if self._cords[2] < 0:
            self._cords[2] = 0
        self.speed /= 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        super().dive_in(dz)

    def lay_eggs(self):
        super().lay_eggs()

    def attack(self):
        super().attack()

    def speak(self):
        super().speak()

    def move(self, dx, dy, dz):
        super().move(dx, dy, dz)

    def get_cords(self):
        super().get_cords()

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(60)
db.get_cords()

db.lay_eggs()

print(Duckbill.mro())