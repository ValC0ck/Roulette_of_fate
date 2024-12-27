import random
import time
from time import sleep


def choice_from_variants(arr: list) -> str:
    index_of_choice = random.randint(0, len(arr) - 1)
    choice = arr[index_of_choice]
    return choice

count_of_variants: int = 0
variant: str = ""
variants: list = []

variant = input("Вводите варианты: ").lower()
while variant.lower() != "stop":
    variants.append(variant)
    variant = input().lower()

count_of_variants = len(variants)

for i in range(10):
    print(choice_from_variants(variants))
    sleep(1)
print(f"ПОБЕДИТЕЛЬ: ***{choice_from_variants(variants)}***")
print(f"ШАНС: {1/count_of_variants * 100}%")