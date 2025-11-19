def bubbleSort(arr):
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


def quickSort(arr):
    new_arr = arr.copy()

    if len(new_arr) <= 1:
        return new_arr

    mid = arr[len(arr)//2]
    l, r = [i for i in arr if i < mid], [i for i in arr if i > mid]
    return quickSort(l) + [mid] + quickSort(r)


def countingSort(arr):
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


def run():
    return 0

if __name__ == "__main__":
    run()