# 6 - Создать список из элементов
list_a = [1,2,3,4,4,5,2,1,8]

# a - Вывести только уникальные значения и сохранить их в отдельную переменную
print("Часть a")
# Set (множество) содержит только уникльные значения
# Создание set через конструктор
set_a = set(list_a)
print(set_a)
# b - Добавить в полученный объект значение 22
print("Часть b")
# Добавление в сет значения через функцию add()
set_a.add(22)
print(set_a)
# c - Сделать list_a неизменяемым
print("Часть c")
# Кортеж - это неизменяемый объект
# Создать кортеж через конструктор tuple()
set_a = tuple(set_a)
print(type(set_a))
# d - Измерить его длину
print("Часть d")
# Выведение длины объекта через функцию len()
print(len(set_a))