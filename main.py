import random
import time
from time import sleep


def choice_from_variants(arr: list) -> str:
    index_of_choice = random.randint(0, len(arr) - 1)
    choice = arr[index_of_choice]
    return choice

def edit_array(arr: list) -> list:
    elem = ""
    while elem.lower() != "stop":
        print("Выберите элемент для редактирования")
        elem = input()
        choice = int(elem)
        if elem == "0":
            break
        while choice > len(arr):
            print("Такого элемента нет")
            choice = int(input())

        index_of_elem = choice - 1

        print("1. Редактировать\n"
              "2. Удалить")
        action = int(input())
        if action == 1:
            arr[index_of_elem] = input()
            print("Редактировние успешно!")
            print_array(arr)
        elif action == 2:
            arr.pop(index_of_elem)
            print("Удаление успешно!")

def print_array(arr: list):
    for i in range(len(variants)):
        print(f"{i + 1}: {variants[i]}")

count_of_variants: int = 0
variant: str = ""
variants: list = []

variant = input("Вводите варианты: ").lower()
while variant.lower() != "stop" and variant.lower() != "стоп":
    variants.append(variant)
    variant = input().lower()

count_of_variants = len(variants)

print(f"Правильный список?:")
print_array(variants)
print(f"1 - ДА\n2 - НЕТ")
answer = int(input())
if answer == 2:
    edit_array(variants)
else:
    for i in range(10):
        print(choice_from_variants(variants))
        sleep(1)
    print(f"ПОБЕДИТЕЛЬ: ***{choice_from_variants(variants)}***")
    print(f"ШАНС: {1/count_of_variants * 100}%")