import random
from timeit import default_timer as timer

def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):
        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False
        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1


if __name__ == '__main__':
    print("Shaker sorting")
    arr = []
    length = 128000
    length_list = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]

    for i in range(0, 20):
        my_file = open(f"{length}.txt", "a+")

        arr.clear()
        for j in range(0, length):
            element = random.uniform(-1.0, 1.0)
            arr.append(element)

        start = timer()
        shaker_sort(arr)
        end = timer()



        print("Sorted array: ")
        print(*arr, sep='\n')
        print(f"Sorting time: {round(end - start, 5)} seconds")

        my_file.write(f"{i + 1}. Sorting time: {round(end - start, 5)} seconds\n")
        my_file.close()