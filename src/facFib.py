def factorial(n):
    if not isinstance(n, int):
        return "n must be an integer"
    elif n < 0:
        return "n must be positive"
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

def factorial_rec(n):
    if not isinstance(n, int):
        return "n must be an integer"
    elif n < 0:
        return "n must be positive"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

def fibo(n):
    if not isinstance(n, int):
        return "n must be an integer"
    elif n < 0:
        return "n must be positive"
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

def fibo_rec(n):
    if not isinstance(n, int):
        return "n must be an integer"
    elif n < 0:
        return "n must be positive"
    elif n == 1 or n == 0:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)


def test_fact_fibo(n):
    #Вывод факториалов
    print(factorial(n))
    print(factorial_rec(n))
    print(factorial_rec(n) == factorial(n))
    #Вывод числа Фибоначчи
    print(fibo(n))
    print(fibo_rec(n))
    print(fibo_rec(n) == fibo(n))


if __name__ == "__main__":
    test_fact_fibo()