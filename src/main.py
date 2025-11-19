from src.facFib import factorial, factorial_rec, fibo, fibo_rec
from src.sortFunnctions import bubbleSort, quickSort, countingSort
from src.constants import FACTRORIALTEST, FIBTEST, NEEDSORT


def main():
    check = {"factorial": True, 'fibo': True, 'bubble_sort': True, 'quick_sort': True, 'counting_sort': True}
    # Проверка функций для подсчета факториала
    for num in FACTRORIALTEST:
        if factorial(num) != factorial_rec(num):
            print("\033[31m{}".format(f'При num = {num} факториалы различны'))
            check['factorial'] = False
    # Проверка функций для подсчета числа Фибоначчи
    for num in FIBTEST:
        if fibo(num) != fibo_rec(num):
            print("\033[31m{}".format(f'При num = {num} числа Фибоначчи различны'))
            check['fibo'] = False


    # Проверка сортировки пузырьком
    if bubbleSort(NEEDSORT) != sorted(NEEDSORT):
        print("\033[31m{}".format('Сортировка пузырьком не работает'))
        check['bubble_sort'] = False

    # Проверка быстрой сортировки
    if quickSort(NEEDSORT) != sorted(NEEDSORT):
        print("\033[31m{}".format('Быстрая сортировка не работает'))
        check['quick_sort'] = False

    # Проверка сортировки счетом
    if countingSort(NEEDSORT) != sorted(NEEDSORT):
        print("\033[31m{}".format('Сортировка подсчетом не работает'))
        check['counting_sort'] = False





    for func, res in check.items():
        if res:
            print("\033[32m{}".format(f'{func} работает исправно'))


if __name__ == "__main__":
    main()