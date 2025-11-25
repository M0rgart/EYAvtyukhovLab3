import random
import time


def rand_int_array(n: int, lo: int, hi: int, *args, distinct=False, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError('Невозможно сгенерировать массив с уникальными элементами')
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *args, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n: int, k_unique = 5, *args, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)
    unique = random.sample(range(n * 10), k_unique)
    return [random.choice(unique) for _ in range(n)]

def reverse_sorted(n: int) -> list[int]:
    return list(range(n-1, -1, -1))

def rand_float_array(n: int, lo=0.0, hi=1.0, *args, seed=None) -> list[float]:
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]


def timeit_once(func, *args, **kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, dict[str, float]]]:
    res = {}
    for algo_name, algo_func in algos.items():
        res[algo_name] = {}
        for array_name, array in arrays.items():
            try:
                time_taken = timeit_once(algo_func, array)
                res[algo_name][array_name] = time_taken
            except Exception as e:
                res[algo_name][array_name] = float('inf')
                print("ERROR:", e)

    return res


def run():
    return 0

if __name__ == "__main__":
    run()