#Задача 1

#Раздел: Создание строки

# Создай переменную word и присвой ей строку "Python".
# Создай переменную empty и присвой ей пустую строку.
# Выведи на экран обе переменные.

word = "Python"
empty = ""

print(word)
print(empty)

# Задача 2
# Раздел: Получение длины строки
#
# Дана строка:
# text = "automation"
#
# Получи длину этой строки и сохрани результат в переменную length.
# Выведи на экран переменную length.

text = "automation"
length = len(text)
print(length)


# Задача 3
# Раздел: Конкатенация строк
#
# Даны две строки:
# first = "Hello"
# second = "World"
#
# Соедини их в одну строку так, чтобы между словами был пробел.
# Сохрани результат в переменную result.
# Выведи на экран переменную result.

first = "Hello"
space = " "
second = "World"

result = first + space + second
print(result)

first = "Hello "
second = "World"
result = first + second
print(result)


# Задача 4
# Раздел: Доступ к символам
#
# Дана строка:
# word = "keyboard"
#
# Выведи на экран первый символ этой строки.
# Выведи на экран последний символ этой строки.

word = "keyboard"
first_letter = word[0]
last_letter = word[-1]
print(first_letter)
print(last_letter)


# Задача 5
# Раздел: F-строки
#
# Даны переменные:
# name = "Anna"
# age = 25
#
# Используя f-строку, выведи на экран фразу в формате:
# My name is Anna, I am 25 years old.

name = "Anna"
age = 25

text = f"My name is {name}, I am {age} years old."
print(text)

# Задача 6
# Раздел: Срезы
#
# Дана строка:
# text = "programming"
#
# Выведи на экран первые 4 символа этой строки, используя срез.

text = "programming"
letters = text[0:4]
print(letters)


# Задача 7
# Раздел: Базовые методы строк
#
# Дана строка:
# text = "  Python Automation  "
#
# Убери пробелы в начале и в конце строки.
# Сохрани результат в переменную clean_text.
# Выведи на экран переменную clean_text.

text = "  Python Automation  "
clean_text = text.strip()
print(clean_text)

