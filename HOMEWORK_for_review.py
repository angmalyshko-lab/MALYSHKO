# ЗАДАЧА 1
number = 42
number_str = str(number)

text = "The answer is: "

result = text + number_str

print(number, type(number))
print(number_str, type(number_str))
print(text, type(text))
print(result, type(result))

# ЗАДАЧА 2
name = "Анжелика"
age = 31
print(f"Меня зовут {name}, мне {age}.")

# ЗАДАЧА 3
my_list = [1, 2, 3]
copy_of_my_list = my_list.copy()
copy_of_my_list[0] = 10
print(my_list, copy_of_my_list)

# ЗАДАЧА 4
m = 14
if m > 0:
    print("Положительное")
elif m == 0:
    print("Ноль")
else:
    print("Отрицательное")

# ЗАДАЧА 5
person = {
   	"name": {
       	"first_name": "Иван",
       	"last_name": "Иванов"
 },
    "address": {
    	"city": "Москва",
   	"country": "Россия"
 	}
 }
person["address"]["city"] = "Санкт-Петербург"
person["address"]["postal_code"] = "333777"
print(person)
del person["address"]["city"]
print(person)

# ЗАДАЧА 6
r = 1
while r <= 20:
    if r % 4 == 0:
        r += 1
        continue
    print(r)
    r += 1

# ЗАДАЧА 7
with open("fruits.txt","w") as file:
    file.write("яблоко")
    file.write("\nбанан")
    file.write("\nапельсин")
with open("fruits.txt","r") as file:
    for line in file:
        print(line.strip())

# ЗАДАЧА 8
def greet_user(user_role,user_name=None):
    if user_name:
        print(f"Привет, {user_name}! Ваша роль: {user_role}.")
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")
greet_user("админ", "flambo")

# ЗАДАЧА 9
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
i_am = Student("Анжелика", 31)
print(i_am.name)
print(i_am.age)

# ЗАДАЧА 10
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        print(f"{self.name} ест.")
    def sleep(self):
        print(f"{self.name} спит.")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} гавкает: Ауф!")


my_dog = Dog("Черри", "Дворняга")

my_dog.eat()
my_dog.sleep()
my_dog.bark()







