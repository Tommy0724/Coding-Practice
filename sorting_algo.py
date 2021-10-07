from time import time
import random


def make_array(num, low, high):
    output = []
    for i in range(num):
        output.append(random.randint(low, high))
    return output


def bubble_sort(arr):
    # Time: O(n**2)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    # Time: O(n**2)
    for i in range(len(arr)):
        selected = arr[i]
        ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < selected:
                selected = arr[j]
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]
    return arr


def quick_sort(arr):
    # Time: O(nlogn)
    if not arr:
        return []
    pivot = arr[-1]
    first_half = []
    second_half = []
    for i in range(len(arr) - 1):
        if pivot > arr[i]:
            first_half.append(arr[i])
        else:
            second_half.append(arr[i])
    return quick_sort(first_half) + [pivot] + quick_sort(second_half)


def heap_sort(arr):
    return arr

def print_info(sorted_arr, time, name, print_result=True):
    print(name, " execution time: ", time)
    if print_result:
        print(name, " sorted result: ", sorted_arr)


def print_execute_time(algo, arr, print_arr=False):
    if algo == 'bubble_sort':
        t1 = time()
        sorted_arr = bubble_sort(arr)
        t2 = time()
        print_info(sorted_arr, t2 - t1, "Bubble Sort", print_arr)
    elif algo == 'selection_sort':
        t1 = time()
        sorted_arr = selection_sort(arr)
        t2 = time()
        print_info(sorted_arr, t2 - t1, "Selection Sort", print_arr)
    elif algo == 'quick_sort':
        t1 = time()
        sorted_arr = quick_sort(arr)
        t2 = time()
        print_info(sorted_arr, t2 - t1, "Quick Sort", print_arr)
    else:
        raise ValueError("Algorithm not found")


if __name__ == '__main__':
    arr = make_array(100, -20, 15)
    print_execute_time('bubble_sort', arr, print_arr=True)
    print_execute_time('selection_sort', arr, print_arr=True)
    print_execute_time('quick_sort', arr, print_arr=True)
    print_execute_time('heap_sort', arr, print_arr=True)
