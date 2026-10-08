# Задача 1.

# Создай класс Animal с методом speak(), который выводит на экран строку "..." (животное издаёт звук).
# Затем создай класс Dog, который наследуется от Animal и переопределяет метод speak(),
# чтобы он выводил "Гав!".
#
# Создай объект класса Dog и вызови у него метод speak().

class Animal:
    def speak(self):
        print("...")
class Dog(Animal):
    def speak(self):
        print("Гав!")
my_dog = Dog()
my_dog.speak()

# Задача 2.

# Создай класс Vehicle с методом move(), который выводит "Транспорт движется".
# Создай класс Car, который наследуется от Vehicle, но НЕ переопределяет метод move().
#
# Создай объект класса Car и вызови у него метод move().
# Посмотри, что выведется — и подумай почему.

class Vehicle:
    def move(self):
        print("Транспорт движется")
class Car(Vehicle):
    pass
my_car = Car()
my_car.move() #вывелось сообщение из родительского класса, так как дочернему не было назначено своё сообщение

# Задача 3.

# Создай класс Person с методом __init__, который принимает имя (name) и сохраняет его в атрибут self.name.
# Также добавь метод introduce(), который выводит "Меня зовут <name>".
#
# Затем создай класс Student, который наследуется от Person.
# В классе Student добавь свой __init__, который принимает name и grade (класс обучения),
# сохраняет grade в self.grade и вызывает __init__ родителя, чтобы сохранить name.
#
# Создай объект Student с именем "Аня" и grade = 10.
# Вызови у него метод introduce() и выведи его атрибут grade.

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Меня зовут {self.name}")
class Student(Person):
    def __init__(self, name, grade):
        self.grade = grade
        super().__init__(name)
the_student = Student("Аня", 10)
the_student.introduce()
print(the_student.grade)

# Задача 4.

# Создай класс Shape с методом area(), который выводит "Площадь неизвестна".
# Создай класс Rectangle, который наследуется от Shape.
# В Rectangle добавь __init__, принимающий width и height, и сохрани их в атрибуты.
# Переопредели метод area() так, чтобы он выводил площадь прямоугольника (width * height).
#
# Создай объект Rectangle с шириной 4 и высотой 5.
# Вызови у него метод area().

class Shape:
    def area(self):
        print("Площадь неизвестна")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print(self.width * self.height)
the_rectangle = Rectangle(4, 5)
the_rectangle.area()