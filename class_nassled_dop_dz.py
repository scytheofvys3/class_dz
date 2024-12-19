import math
class Figure:
    sides_count = 0
    def __init__(self, __color, __sides):
        self.__sides = list(__sides)
        self.__color = [*__color]
        self.filled = True

    def check(self):
        l = 0
        if len(self.__sides) == self.sides_count:
            for i in self.__sides:
                self.__sides = []
                self.__sides.append(i)
                return self.__sides
        else:
            self.__sides = []
            while l < self.sides_count:
                self.__sides.append(1)
                l += 1
            return self.__sides

        # l = 0
        # if self.sides_count == len(self.__sides):
        #     for i in self.__sides:
        #         self.__sides = []
        #         while l < self.sides_count:
        #             self.__sides.append(i)
        #             l += 1
        #         return self.__sides
        # else:
        #     for i in self.__sides:
        #         self.__sides = []
        #         while l < self.sides_count:
        #             u = i
        #             self.__sides.append(u)
        #             l += 1
        #         return self.__sides



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = []
                self.__color.append(r)
                self.__color.append(g)
                self.__color.append(b)
                return self.__color
            else:
                return self.__color

    def set_color(self, r, g ,b):
        self.__is_valid_color(r, g, b)

    def __is_valid_sides(self, *args):
        for i in args:
            if i > 0 and len(args) == len(self.__sides):
                return True
        else:
            return False

    def get_sides(self):
        return self.__sides ###

    def __len__(self):
        j = 0
        for i in self.__sides:
            j += i
        return j

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = [*new_sides]
            return self.__sides
        else:
            return self.__sides


class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        super().check()
        storona = __sides[0]
        self.__radius = int(storona) * 3.14 / 1


    def get_square(self):
        sq = 3.14 * self.__radius ** 2
        return sq

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        super().check()

    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        s = math.sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2]))
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *__sides):
        x = len(__sides)
        if x == 1:
            self.__sides = list(__sides)
            for i in self.__sides:
                self.__sides = []
                l = 0
                while l < self.sides_count:
                    self.__sides.append(i)
                    l += 1
                super().__init__(__color, self.__sides)
        else:
            super().__init__(__color, __sides)
            super().check()

    def get_volume(self):
        return self.__sides[0] ** 3

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
#
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(circle1.get_square())

print('------------------------------------')

circle2 = Circle((200, 200, 100), 15, 10)
print(circle2.get_sides())
triangle = Triangle((200, 200, 100), 10, 6)
print(triangle.get_sides())
cube2 = Cube((200, 200, 100), 9)
print(cube2.get_sides())
print(cube2.get_volume())
cube3 = Cube((200, 200, 100), 12)
print(cube3.get_sides())
print(cube3.get_volume())
print(cube3.__len__())