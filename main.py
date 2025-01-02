import random
import time
from time import sleep

# функция выбирает случайный элемент из массива
def choice_from_variants(arr: list) -> str:
    index_of_choice = random.randint(0, len(arr) - 1)
    choice = arr[index_of_choice]
    return choice

# функция редактирует элементы массива по порядковому номеру в массиве
# 1. Удаляет элемент
# 2. Редактирует элемент
def edit_array(arr: list) -> list:
    elem = ""
    while elem.lower() != "stop":
        print("Выберите элемент для редактирования.\n"
              "Для выхода введите: 0")
        elem = input()
        choice = int(elem)
        # завершаем работу функции, если юзер ввел 0
        if choice == 0:
            break

        # проверяем, если пользователь ввел номер
        # которого нет в массиве
        while choice > len(arr):
            print("Такого элемента нет")
            choice = int(input())

        # мини-костыль
        index_of_elem = choice - 1

        print("1. Редактировать\n"
              "2. Удалить")

        action = int(input())
        if action == 1:
            arr[index_of_elem] = input("Новое значение: ")
            print("Редактировние успешно!")
        elif action == 2:
            arr.pop(index_of_elem)
            print("Удаление успешно!")
        print_array(arr)

# функция выводит список
def print_array(arr: list):
    for i in range(len(variants)):
        print(f"{i + 1}: {variants[i]}")

count_of_variants: int = 0
variant: str = ""
variants: list = []

# просим пользователя вводить варианты
variant = input("Вводите варианты\n"
                "Если закончили - введите \"стоп\"\n").lower()
while variant.lower() != "stop" and variant.lower() != "стоп":
    variants.append(variant)
    variant = input().lower()

count_of_variants = len(variants)

# если элементов 0
if count_of_variants == 0:
    exit()

# спрашиваем пользователя, хочет ли он
# отредактировать список
print(f"Редактировать список?:")
print_array(variants)
print(f"1 - ДА\n2 - НЕТ")
answer = int(input())
if answer == 1:
    edit_array(variants)
for i in range(5):
    print(choice_from_variants(variants))
    sleep(1)

# обновляем эту переменную, т.к. кол-во элементов
# могло измениться
count_of_variants = len(variants)
print(f"ПОБЕДИТЕЛЬ: ***{choice_from_variants(variants)}***")
print(f"ШАНС: {1/count_of_variants * 100}%")