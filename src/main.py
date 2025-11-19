from src.facFib import factorial, factorial_rec, fibo, fibo_rec
from src.constants import FACTRORIALTEST, FIBTEST


def main():
    check = {"factorial": True, 'fibo': True}
    for num in FACTRORIALTEST:
        if factorial(num) != factorial_rec(num):
            print("\033[31m{}".format(f'При num = {num} факториалы различны'))
            check['factorial'] = False

    for num in FIBTEST:
        if fibo(num) != fibo_rec(num):
            print("\033[31m{}".format(f'При num = {num} числа Фибоначчи различны'))
            check['fibo'] = False

    for func, res in check.items():
        if res:
            print("\033[32m{}".format(f'{func} работает исправно'))


if __name__ == "__main__":
    main()