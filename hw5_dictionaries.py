# Задача 1

# Создай пустой словарь с именем student.

# Затем добавь в него три элемента:
# - ключ "name" со значением "Анна"
# - ключ "age" со значением 20
# - ключ "city" со значением "Москва"

# После этого выведи получившийся словарь на экран.

student = {
}
student["name"] = "Анна"
student["age"] = 20
student["city"] = "Москва"
print(student)


# Задача 2

# Дан словарь:
#car = {
#   "brand": "Toyota",
#   "model": "Camry",
#   "year": 2020
#}

# Выведи на экран:
# 1) значение по ключу "brand"
# 2) значение по ключу "year"

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print(car["brand"])
print(car["year"])

# Задача 3

# Дан словарь:
#phone = {
#    "brand": "Samsung",
#    "model": "Galaxy S21",
#    "price": 50000
#}

# 1) Измени значение по ключу "price" на 45000
# 2) Добавь новый элемент с ключом "color" и значением "black"
# 3) Выведи получившийся словарь на экран

phone = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "price": 50000
}

phone["price"] = 45000
phone["color"] = "black"
print(phone)


# Задача 4

# Дан словарь:
#user = {
#    "name": "Иван",
#    "age": 25,
#    "email": "ivan@mail.ru"
#}

# 1) Удали элемент по ключу "email"
# 2) Выведи получившийся словарь на экран
# 3) Проверь, остался ли ключ "email" в словаре — выведи результат проверки

user = {
    "name": "Иван",
    "age": 25,
    "email": "ivan@mail.ru"
}

del user["email"]
print(user)

if "email" in user:
    print("ключ есть")
else:
    print("ключ отсутствует")


# Задача 5

# Дан словарь:
#fruit_prices = {
#    "apple": 50,
#    "banana": 30,
#    "orange": 70
#}

# 1) Выведи на экран все ключи словаря
# 2) Выведи на экран все значения словаря
# 3) Выведи на экран все пары ключ-значение словаря

fruit_prices = {
    "apple": 50,
    "banana": 30,
    "orange": 70
}
keys = fruit_prices.keys()
print(keys)
values = fruit_prices.values()
print(values)
items = fruit_prices.items()
print(items)


# Задача 6

# Дан словарь:
#settings = {
#    "theme": "dark",
#    "language": "ru",
#   "font_size": 14
#}

# 1) Проверь, есть ли в словаре ключ "theme" — выведи результат проверки
# 2) Проверь, есть ли в словаре ключ "volume" — выведи результат проверки
# 3) Проверь, есть ли в словаре значение "ru" — выведи результат проверки

settings = {
    "theme": "dark",
    "language": "ru",
    "font_size": 14
}
if "theme" in settings:
    print("тема есть")
if "volume" in settings:
    print("громкость есть")
print("ru" in settings.values())