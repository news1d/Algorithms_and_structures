from sha1 import SHA1
import random
import string
from prettytable import PrettyTable
import time
import matplotlib.pyplot as plt

# Функция для генерации случайных строк
def random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Функция для генерации пар строк с различным количеством отличий
def generate_pairs(num_pairs, num_diff):
    pairs = []
    for i in range(num_pairs):
        str1 = random_string(128)
        str2 = list(str1)
        for j in range(num_diff):
            idx = random.randint(0, 127)
            str2[idx] = random.choice(string.ascii_letters + string.digits)
        str2 = ''.join(str2)
        pairs.append((str1, str2))
    return pairs

# Функция для вычисления хеша SHA-1 для строки
def sha1_hash(str):
    sha1 = SHA1(str)
    return sha1.final_hash()


if __name__ == '__main__':
    # --------------ТЕСТ №1--------------
    # Список количества отличий
    num_diffs = [1, 2, 4, 8, 16]

    # Список максимальной длины одинаковой последовательности символов для каждого количества отличий
    max_lengths = []

    for diff in num_diffs:
        pairs = generate_pairs(1000, diff)
        max_length = 0
        for pair in pairs:
            hash1 = sha1_hash(pair[0])
            hash2 = sha1_hash(pair[1])
            length = 0
            for i in range(40):
                if hash1[i] == hash2[i]:
                    length += 1
                else:
                    if length > max_length:
                        max_length = length
                    length = 0
        max_lengths.append(max_length)

    # Рисуем график
    plt.title("Максимальная длина идентичной последовательности")
    plt.plot(num_diffs, max_lengths)
    plt.xlabel('Количество различий')
    plt.ylabel('Максимальная длина')
    plt.show()

    # --------------ТЕСТ №2--------------
    # Создаем таблицу
    table = PrettyTable()
    table.field_names = ["Кол-во генераций", "Кол-во дубликатов"]

    # Создаем N случайных строк и добавляем их хеши в список
    for i in range(2, 7):
        N = 10 ** i
        # Создаем список хешей
        hash_list = []
        for j in range(N):
            str = random_string(256)
            hash = sha1_hash(str)
            hash_list.append(hash)

        # Ищем дубликаты хешей
        duplicates = set()
        for x in hash_list:
            if hash_list.count(x) > 1:
                duplicates.add(x)

        # Добавляем результаты в таблицу
        table.add_row([N, len(duplicates)])

    # Печатаем таблицу
    print(table)

    # --------------ТЕСТ №3--------------
    # Список длин строк для генерации хеша
    string_lengths = [64, 128, 256, 512, 1024, 2048, 4096, 8192]

    # Пустые списки для хранения средних времен генерации хеша и размеров входных данных
    mean_times = []
    data_sizes = []

    # Проходим по каждой длине строки и генерируем по 1000 хешей для каждой длины
    for length in string_lengths:
        times = []
        for i in range(1000):
            # Генерируем случайную строку заданной длины
            str = random_string(length)

            start_time = time.time()
            hash = sha1_hash(str)
            end_time = time.time()
            times.append(end_time - start_time)

        # Вычисляем среднее время генерации хеша для данной длины строки
        mean_time = sum(times) / len(times)

        # Добавляем результаты в список
        mean_times.append(mean_time)
        data_sizes.append(length)

    # Построение графика
    plt.plot(data_sizes, mean_times)
    plt.xlabel("Размер строки (символы)")
    plt.ylabel("Среднее время генерации хеша (мс)")
    plt.title("Зависимость скорости расчета хеша от размера строки")
    plt.show()