import inspect
import sys
sys.setrecursionlimit(1000000) # 10000 is an example, try with different values

import random

def quick_sort(array):
    quick_sort.recursion_counter += 1

    if len(array) <= 1:
        # if (len(inspect.stack()) > quick_sort.deep_max):
        #     quick_sort.deep_max = len(inspect.stack())
        return array

    elem = array[len(array) // 2]
    left = [i for i in array if i < elem]
    center = [i for i in array if i == elem]
    right = [i for i in array if i > elem]

    return quick_sort(left) + center + quick_sort(right)

def generation(array, length, gener_type):
    if gener_type == 1:
        for i in range(0, length):
            element = random.uniform(-1.0, 1.0)
            array.append(element)
        array.sort()
        return array
    elif gener_type == 2:
        for i in range(0, length):
            element = 0.5
            array.append(element)
        return array
    elif gener_type == 3:
        array.append(-1.0 + 2.0 / length)
        for i in range(1, length):
            element = array[i - 1] + 2.0 / length
            array.append(element)
        for i in range(0, length - 1):
            array[i], array[i // 2] = array[i // 2], array[i]
        return array
    elif gener_type == 4:
        my_dict = {}
        for i in range(1, length + 1):
            my_dict[i] = 0
        counter = 0
        for i in range(0, length):
            counter += 1
            my_dict[list(my_dict.keys())[0]] = len(my_dict) - counter + 1
            new_tuple = list(my_dict.items())
            new_tuple[0], new_tuple[length - i - 1] = new_tuple[length - i - 1], new_tuple[0]
            my_dict = dict(new_tuple)

        my_dict = dict(sorted(my_dict.items()))
        array = list(my_dict.values())
        return array
    elif gener_type == 5:
        for i in range(0, length):
            element = random.uniform(-1.0, 1.0)
            array.append(element)
        return array

if __name__ == '__main__':
    length_list = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
    gener_type = 1
    quick_sort.recursion_counter = 0
    quick_sort.deep_max = 0

    my_file = open(f"test_{gener_type}.txt", "a+")
    my_file.write("{: ^10} {: ^10} {: ^10} {: ^10}".format('N', 'MAX', 'AVG', 'MIN') + '\n')
    for i in range(len(length_list)):
        sum_recursion = 0
        max_recursion = 0
        min_recursion = 9999999
        for j in range(0, 1):

            arr = []
            arr = generation(arr, length_list[i], gener_type)

            quick_sort.recursion_counter = 0
            quick_sort.deep_max = 0

            print(*arr)
            arr = quick_sort(arr)

            if quick_sort.recursion_counter > max_recursion:
                max_recursion = quick_sort.recursion_counter

            if quick_sort.recursion_counter < min_recursion:
                min_recursion = quick_sort.recursion_counter

            sum_recursion += quick_sort.recursion_counter

            print("Sorted array: ")
            print(*arr)
            print(quick_sort.recursion_counter)
            print(f"{quick_sort.deep_max}\n")

        my_file.write("{: ^10} {: ^10} {: ^10} {: ^10}".format(length_list[i], max_recursion, (sum_recursion // 20), min_recursion) + '\n')
        print(f"N MAX AVG MIN\n{length_list[i]} {max_recursion} {sum_recursion // 1} {min_recursion}\n")
    my_file.close()