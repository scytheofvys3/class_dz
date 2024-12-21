class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    def __repr__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        rfile = file.read()
        file.close()
        return rfile

    def add(self, *other):
        existing_products = self.get_products()
        for i in other:
            if isinstance(i, Product):
                if i.name in existing_products:
                     print(f'Продукт {i.name} уже есть в магазине')
                else:
                    file = open(self.__file_name, 'a')
                    file.write(f'{i.name}, {i.weight}, {i.category}\n')
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())






