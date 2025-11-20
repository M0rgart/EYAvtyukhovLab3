def bubbleSort(arr: list[int]) -> list[int]:
    n = len(arr)
    new_arr = arr.copy()
    for i in range(n):
        changed = True
        for j in range(0, n-i-1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
                changed = False
        if changed:
            break
    return new_arr


def quickSort(arr: list[int]) -> list[int]:
    new_arr = arr.copy()

    if len(new_arr) <= 1:
        return new_arr

    mid = arr[len(arr)//2]
    l, r = [i for i in arr if i < mid], [i for i in arr if i > mid]
    return quickSort(l) + [mid] + quickSort(r)


def countingSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr.copy()

    mn, mx = min(arr), max(arr)
    rng = mx - mn + 1
    cnt = [0] * rng

    for num in arr:
        cnt[num - mn] += 1

    pre = [0] * rng
    pre[0] = cnt[0]
    for i in range(1, rng):
        pre[i] = pre[i - 1] + cnt[i]

    new_arr = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        new_arr[pre[arr[i] - mn] - 1] = arr[i]
        pre[arr[i] - mn] -= 1

    return new_arr


def radix_sort(arr: list[int], base: int = 10) -> list[int] or []:
    if len(arr) <= 1:
        return arr
    elif min(arr) < 0:
        raise ValueError("Radix sort can only be applied to positive numbers")
    else:
        new_arr = arr.copy()
        mx = max(new_arr)
        x = 1

        while mx // x > 0:
            lst =  [[] for _ in range(base)]
            for num in new_arr:
                lst[(num // x) % base].append(num)

            new_arr = []
            for i in lst:
                new_arr.extend(i)

            x *= base
        return new_arr


def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]:
    if len(arr) <= 1:
        return arr
    else:
        new_arr = arr.copy()
        n = len(arr)

        if buckets is None:
            buckets = n

        mn, mx = min(new_arr), max(new_arr)
        lst = [[] for _ in range(buckets)]

        for num in new_arr:
            idx = int((num - mn) / (mx - mn) * (buckets - 1))
            lst[idx].append(num)

        new_arr = []
        for bucket in lst:
            new_arr.extend(bubbleSort(bucket))

        return new_arr


def heap_sort(arr: list[int]) -> list[int]:
    new_arr = arr.copy()
    n = len(new_arr)

    def heap(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heap(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heap(new_arr, n, i)

    for i in range(n - 1, 0, -1):
        new_arr[i], new_arr[0] = new_arr[0], new_arr[i]
        heap(new_arr, i, 0)

    return new_arr




def run():
    return 0

if __name__ == "__main__":
    run()