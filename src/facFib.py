def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

def fibo_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")
    elif n == 1 or n == 0:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

def run():
    return 0

if __name__ == "__main__":
    run()