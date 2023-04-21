from binary import BinaryHeapMax
from binomial import BinomialHeap
import random
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    count_items = []

    # Списки для хранения времени вставки в бинарную и биномальную кучу
    insert_time_avg_binar = []
    insert_time_avg_binom = []

    insert_time_max_binar = []
    insert_time_max_binom = []

    # Списки для хранения времени поиска в бинарной и биномальной куче
    search_time_avg_binar = []
    search_time_avg_binom = []

    search_time_max_binar = []
    search_time_max_binom = []

    # Списки для хранения времени удаления в бинарной и биномальной куче
    delete_time_avg_binar = []
    delete_time_avg_binom = []

    delete_time_max_binar = []
    delete_time_max_binom = []

    for i in range(3, 8):
        print(f"Тест №{i - 2}")
        count_items.append(10 ** i)

        # Временные списки для хранения времени вставки в бинарную и биномальную кучу
        insert_time_binar_tmp = []
        insert_time_binom_tmp = []

        # Временные списки для хранения времени поиска в бинарной и биномальной куче
        search_time_binar_tmp = []
        search_time_binom_tmp = []

        # Временные списки для хранения времени удаления в бинарной и биномальной куче
        delete_time_binar_tmp = []
        delete_time_binom_tmp = []

        num_list = random.sample(range(1, 10**7 + 1000), 10 ** i)

        BinaryH = BinaryHeapMax()
        BinomialH = BinomialHeap()

        # Наполняем кучи
        for x in num_list:
            BinaryH.insert(x)
            BinomialH.insert(x)

        # Замеряем время вставки бинарной кучи
        for x in range(1000):
            rand_number = random.randint(1, 2**7 + 1000)
            start = time.time()
            BinomialH.insert(rand_number)
            end = time.time()
            insert_time_binar_tmp.append(end - start)
        insert_time_avg_binar.append(sum(insert_time_binar_tmp) / len(insert_time_binar_tmp))
        insert_time_max_binar.append(max(insert_time_binar_tmp))

        # Замеряем время вставки биномиальной кучи
        for x in range(1000):
            rand_number = random.randint(1, 2**7 + 1000)
            start = time.time()
            BinomialH.insert(rand_number)
            end = time.time()
            insert_time_binom_tmp.append(end - start)
        insert_time_avg_binom.append(sum(insert_time_binom_tmp) / len(insert_time_binom_tmp))
        insert_time_max_binom.append(max(insert_time_binom_tmp))

        # Замеряем время поиска в бинарной куче
        for x in range(1000):
            start = time.time()
            BinaryH.get_max()
            end = time.time()
            search_time_binar_tmp.append(end - start)
        search_time_avg_binar.append(sum(search_time_binar_tmp) / len(search_time_binar_tmp))
        search_time_max_binar.append(max(search_time_binar_tmp))

        # Замеряем время поиска в биномиальной куче
        for x in range(1000):
            start = time.time()
            BinomialH.get_min()
            end = time.time()
            search_time_binom_tmp.append(end - start)
        search_time_avg_binom.append(sum(search_time_binom_tmp) / len(search_time_binom_tmp))
        search_time_max_binom.append(max(search_time_binom_tmp))

        # Замеряем время удаления в бинарной куче
        for x in range(1000):
            start = time.time()
            BinaryH.delete_max()
            end = time.time()
            delete_time_binar_tmp.append(end - start)
        delete_time_avg_binar.append(sum(delete_time_binar_tmp) / len(delete_time_binar_tmp))
        delete_time_max_binar.append(max(delete_time_binar_tmp))

        # Замеряем время удаления в бинарной куче
        for x in range(1000):
            start = time.time()
            BinomialH.delete_min()
            end = time.time()
            delete_time_binom_tmp.append(end - start)
        delete_time_avg_binom.append(sum(delete_time_binom_tmp) / len(delete_time_binom_tmp))
        delete_time_max_binom.append(max(delete_time_binom_tmp))

    # Строим график для среднего времени вставки
    plt.title("Среднее время вставки")
    plt.plot(count_items, insert_time_avg_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, insert_time_avg_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для максимального времени вставки
    plt.title("Максимальное время вставки")
    plt.plot(count_items, insert_time_max_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, insert_time_max_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для среднего времени поиска
    plt.title("Среднее время поиска")
    plt.plot(count_items, search_time_avg_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, search_time_avg_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для максимального времени поиска
    plt.title("Максимальное время поиска")
    plt.plot(count_items, search_time_max_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, search_time_max_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для среднего времени удаления
    plt.title("Среднее время удаления")
    plt.plot(count_items, delete_time_avg_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, delete_time_avg_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для максимального времени удаления
    plt.title("Максимальное время удаления")
    plt.plot(count_items, delete_time_max_binar, 'o-', label="Бинарная куча")
    plt.plot(count_items, delete_time_max_binom, 'o-', label="Биномиальная куча")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()




