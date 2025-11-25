from src.facFib import factorial, factorial_rec, fibo, fibo_rec
from src.sortFunnctions import bubbleSort, quickSort, countingSort, radix_sort, bucket_sort, heap_sort
from src.constants import FACTRORIALTEST, FIBTEST, NEEDSORT, NEEDSORTPOS, NEEDSORTBUCKET
from src.structures import Stack, Queue


def main():
    check = {"factorial": True, 'fibo': True, 'bubble_sort': True, 'quick_sort': True, 'counting_sort': True,
             "radix_sort": True, "bucket_sort": True, "heap_sort": True}

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

    # Проверка поразрядной сортировки
    if radix_sort(NEEDSORTPOS) != sorted(NEEDSORTPOS):
        print("\033[31m{}".format('Поразрядная сортировка не работает'))
        check['radix_sort'] = False

    # Проверка сортировки блоками
    if bucket_sort(NEEDSORTBUCKET) != sorted(NEEDSORTBUCKET):
        print("\033[31m{}".format('Сортировка блоками не работает'))
        check['bucket_sort'] = False

    # Проверка сортировки кучами
    if heap_sort(NEEDSORT) != sorted(NEEDSORT):
        print("\033[31m{}".format('Сортировка кучами не работает'))
        check['heap_sort'] = False

    for func, res in check.items():
        if res:
            print("\033[32m{}".format(f'{func} работает исправно'))

    stack = Stack()
    for i in range(1, 5):
        stack.push(i)
    print(f"\nСтек: peek = {stack.peek()}, min = {stack.min()}, len = {stack.__len__()}, is_empty = {stack.is_empty()}")
    print("Pop:", stack.pop(), '\n')

    queue = Queue()
    for i in range(1, 5):
        queue.enqueue(i)
    print(f"Очередь: front = {queue.front()}, len = {stack.__len__()}, is_empty = {stack.is_empty()}")
    print("Dequeue:", queue.dequeue())


if __name__ == "__main__":
    main()