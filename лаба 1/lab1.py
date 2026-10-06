import time
import random
import tracemalloc

#проверка есть ли элемент
def proverka_elementa(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

#2 второй максимум
def poisk_vtorogo_max(arr):
    max1 = arr[0]
    max2 = 0
    for i in range(1, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max2

# 3.бинарный поиск
def binarny_poisk(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#4таблица умножения
def tablica_umnozheniya(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

#5 сортировка вставками (доп задание)
def sortirovka_vstavkami(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

def measure_memory(func, *args):
    tracemalloc.start()
    func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr


if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]

    # 1
    print("1 Поиск элемента")
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(proverka_elementa, arr, 10001)
        m = measure_memory(proverka_elementa, arr, 10001)
        print("n =", n, " время =", t, " память =", m)

    print()

    # 2
    print("2 Второй максимум")
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(poisk_vtorogo_max, arr)
        m = measure_memory(poisk_vtorogo_max, arr)
        print("n =", n, " время =", t, " память =", m)

    print()

    #3
    print("3 Бинарный поиск")
    for n in sizes:
        arr = generate_array(n)
        arr.sort()
        t = measure_time(binarny_poisk, arr, 10001)
        m = measure_memory(binarny_poisk, arr, 10001)
        print("n =", n, " время =", t, " память =", m)

    print()

    # 4
    print("4 Таблица умножения")
    for n in [10, 50, 100, 200]:
        t = measure_time(tablica_umnozheniya, n)
        m = measure_memory(tablica_umnozheniya, n)
        print("n =", n, " время =", t, " память =", m)

    print()

    #5
    print("5 Сортировка вставками")
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(sortirovka_vstavkami, arr.copy())
        m = measure_memory(sortirovka_vstavkami, arr.copy())
        print("n =", n, " время =", t, " память =", m)

    #print("все готово")