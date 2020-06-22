class Animal():
    def __init__(self, name, weight, animal_type, sound):
        self.animal_type = animal_type
        self.name = name
        self.weight = weight
        self.sound = sound

    def sounds(self):
       return f'{self.animal_type} говорит {self.sound}'

    def eating(self, meal, portion):
        return f'{self.animal_type} {self.name} съело {meal} {portion} кг'


class Cow(Animal):
    def __init__(self, name, weight, animal_type='Корова', sound ='Муууу'):
        super().__init__(name, weight, animal_type, sound)

    def milking(self, milk_volume):
        return f'{self.animal_type} дает {milk_volume} Л молока'

class Sheep(Animal):
    def __init__(self, name, weight, animal_type='Овца',sound ='Бееее' ):
        super().__init__(name, weight, animal_type, sound)

    def cutting(self, wool_volume):
        return f'{self.animal_type} дает {wool_volume} килограммов шерсти'

class Goat(Animal):
    def __init__(self, name, weight, animal_type='Коза',sound ='Уууууу' ):
        super().__init__(name, weight, animal_type, sound)

    def milking(self, milk_volume):
        return f'{self.animal_type} дает {milk_volume} Л молока'


class Bird(Animal):
    def __init__(self, name, weight, animal_type, sound):
        super().__init__(name, weight, animal_type, sound)

    def carry_egg(self, eggs_number):
        return f'Собрано {eggs_number} яиц'


class Goose(Bird):
    def __init__(self, name, weight, animal_type='Гусь', sound="Га-га-га"):
        super().__init__(name, weight, animal_type, sound)


class Chicken(Bird):
    def __init__(self, name, weight, animal_type='Курица', sound= 'ко-ко-ко'):
        super().__init__(name, weight, animal_type, sound)


class Duck(Bird):
    def __init__(self, name, weight, animal_type='Утка', sound= 'кря-кря-кря'):
        super().__init__(name, weight, animal_type, sound)


animal_1 = Goose('Серый', 5)
animal_2 = Goose('Белый', 6)
animal_3 = Cow('Манька', 352)
animal_4 = Sheep('Барашек', 35)
animal_5 = Sheep('Кудрявый', 25)
animal_6 = Chicken('Ко-Ко', 2.7)
animal_7 = Chicken('Кукареку', 2.1)
animal_8 = Duck('Кряква', 2.5)
animal_9 = Goat('Рога', 7.4)
animal_10 = Goat('Копыта', 7.4)


print(animal_2.carry_egg(12))
print(animal_1.sounds())
print(animal_5.eating('Овса', 3))
print(animal_3.milking(5.1))
print(animal_9.milking(1.7))
print(animal_4.cutting(5))

animals = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10]

total_weight = 0
for animal in animals:
    total_weight += animal.weight
print(f'Общий вес животных составил: {total_weight:.2f}')

weights = []
for animal in animals:
    weights.append(animal.weight)

for animal in animals:
    if animal.weight == max(weights):
        print(f'Самое тяжелое животное {animal.name}')
    else:
        pass


