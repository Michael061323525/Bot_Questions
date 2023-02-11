# Дополнить базовый класс дополнительными методами. (На свое усмотрение)
# Расширить отнаследованные классы реализациями дополнительных методов.
# Значения переменные объектов записать в файл.
# Запись переменных объектов в файл должна производиться отдельным методом объекта record_to_file
class Animal:
    def __init__(self, name, eyes_color):
        self.name = name
        self.eyes_color = eyes_color

    def call_voice(self):
        pass

    def commands(self):
        pass

    def food(self):
        pass

    def record_to_file(self):
        with open("say.txt", "a+", encoding="utf-8") as file:
            file.write(self.name)
            file.write(self.eyes_color)


class Cat(Animal):

    def call_voice(self):
        print("Мяу")
        return "Мяу"

    def commands(self):
        print("Барсик, сидеть!")
        return "Барсик сел"

    def food(self):
        print("Мяу...")
        return "Барсик хочет есть"

class Dog(Animal):

    def call_voice(self):
        print("Гав")
        return "Гав"

    def commands(self):
        print("Шарик, дай лапу")
        return "Шарик подает лапу"

    def food(self):
        print("Гав...")
        return "Шарик хочет есть"

cat = Cat("Барсик", "Серые")
result_cat_voice = cat.call_voice()
result_cat_commands = cat.commands()
result_cat_food = cat.food()
cat.record_to_file()
dog = Dog("Шарик", "Зеленые")
result_dog_voice = dog.call_voice()
result_dog_commands = dog.commands()
result_dog_food = dog.food()
dog.record_to_file()















