from rand_tree import RandTree
from avl_tree import AVLTree
import sys
import random
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**6) # устанавливаем максимальную глубину рекурсии в 1 миллион вызовов

if __name__ == '__main__':
    count_items = []
    # Списки для хранения времени вставки в AVL дерево и рандомизированое
    insert_time_avl = []
    insert_time_rnd = []

    # Списки для хранения времени поиска в AVL дереве и рандомизированом
    search_time_avl = []
    search_time_rnd = []

    # Списки для хранения времени удаления в AVL дереве и рандомизированом
    delete_time_avl = []
    delete_time_rnd = []

    # Списки для хранения максимальной глубины в AVL дереве и рандомизированом
    max_depth_avl = []
    max_depth_rnd = []

    for i in range(9):
        print(f"Серия №{i + 1}")
        count_items.append(2 ** (10 + i))

        # Временные списки для хранения времени вставки в AVL дерево и рандомизированое
        insert_time_avl_tmp = []
        insert_time_rnd_tmp = []

        # Временные списки для хранения времени поиска в AVL дереве и рандомизированом
        search_time_avl_tmp = []
        search_time_rnd_tmp = []

        # Временные списки для хранения времени удаления в AVL дереве и рандомизированом
        delete_time_avl_tmp = []
        delete_time_rnd_tmp = []

        # Временные списки для хранения максимальной глубины в AVL дереве и рандомизированом
        max_depth_avl_tmp = []
        max_depth_rnd_tmp = []

        # Временные списки для хранения максимальной глубины в AVL дереве и рандомизированом в последней серии тестов
        max_depth_avl_last_tmp = []
        max_depth_rnd_last_tmp = []

        # Временные списки для хранения глубины каждой ветки в AVL дереве и рандомизированом в последней серии тестов
        all_depths_avl_tmp = []
        all_depths_rnd_tmp = []

        for j in range(50):
            num_list = random.sample(range(1, 500000), 2 ** (10 + i))

            AvlTree = AVLTree()
            RndTree = RandTree()
            root = None

            # Замеряем время вставки AVL дерева
            start = time.time()
            for x in num_list:
                AvlTree.insert(x)
            end = time.time()
            insert_time_avl_tmp.append(end - start)

            # Замеряем время вставки рандомизированного дерева
            start = time.time()
            for x in num_list:
                root = RndTree.insert(root, x)
            end = time.time()
            insert_time_rnd_tmp.append(end - start)

            # Замеряем время поиска в AVL дереве
            start = time.time()
            for x in range(1000):
                rand_number = random.randint(1, 500000)
                AvlTree.search(rand_number)
            end = time.time()
            search_time_avl_tmp.append(end - start)

            # Замеряем время поиска в рандомизированном дереве
            start = time.time()
            for x in range(1000):
                rand_number = random.randint(1, 500000)
                node = RndTree.search(root, 10)
            end = time.time()
            search_time_rnd_tmp.append(end - start)

            # Ищем максимальную глубину AVL дерева
            avl_max_depth = AvlTree.max_depth(AvlTree.root)
            max_depth_avl_tmp.append(avl_max_depth)

            # Ищем максимальную глубину рандомизированного дерева
            rnd_max_depth = RndTree.max_depth(root)
            max_depth_rnd_tmp.append(rnd_max_depth)

            # Ищем максимальную глубину дерева и глубину всех веток для последней серии тестов
            if i == 8:
                max_depth_avl_last_tmp.append(avl_max_depth)
                max_depth_rnd_last_tmp.append(rnd_max_depth)

                avl_all_depths = AvlTree.all_depths(AvlTree.root)
                all_depths_avl_tmp.append(sum(avl_all_depths)/len(avl_all_depths))

                rnd_all_depths = RndTree.all_depths(root)
                all_depths_rnd_tmp.append(sum(rnd_all_depths)/len(rnd_all_depths))

            # Замеряем время удаления в AVL дереве
            start = time.time()
            for x in range(1000):
                rand_number = random.randint(1, 500000)
                AvlTree.delete(rand_number)
            end = time.time()
            delete_time_avl_tmp.append(end - start)

            # Замеряем время удаления в рандомизированном дереве
            start = time.time()
            for x in range(1000):
                rand_number = random.randint(1, 500000)
                RndTree.delete(root, rand_number)
            end = time.time()
            delete_time_rnd_tmp.append(end - start)


        # Добавляем среднее значение времени вставки в AVL дерево и рандомизированое
        insert_time_avl.append(sum(insert_time_avl_tmp)/len(insert_time_avl_tmp))
        insert_time_rnd.append(sum(insert_time_rnd_tmp)/len(insert_time_rnd_tmp))

        # Добавляем среднее значение времени поиска в AVL дереве и рандомизированом
        search_time_avl.append(sum(search_time_avl_tmp)/len(search_time_avl_tmp))
        search_time_rnd.append(sum(search_time_rnd_tmp)/len(search_time_rnd_tmp))

        # Добавляем максимальное значение максимальной глубины в AVL дереве и рандомизированом
        max_depth_avl.append(max(max_depth_avl_tmp))
        max_depth_rnd.append(max(max_depth_rnd_tmp))

        try:
            # Добавляем среднее значение максимальной глубины в AVL дереве и рандомизированом в последней серии тестов
            max_depth_avl_last = sum(max_depth_avl_last_tmp)/len(max_depth_avl_last_tmp)
            max_depth_rnd_last = sum(max_depth_rnd_last_tmp)/len(max_depth_rnd_last_tmp)

            # Добавляем среднее значение глубины веток в AVL дереве и рандомизированом в последней серии тестов
            all_depths_avl = sum(all_depths_avl_tmp)/len(all_depths_avl_tmp)
            all_depths_rnd = sum(all_depths_rnd_tmp)/len(all_depths_rnd_tmp)
        except:
            print(i)

        # Добавляем среднее значение времени удаления в AVL дереве и рандомизированом
        delete_time_avl.append(sum(delete_time_avl_tmp)/len(delete_time_avl_tmp))
        delete_time_rnd.append(sum(delete_time_rnd_tmp)/len(delete_time_rnd_tmp))


    # Строим график для вставки
    plt.title("Вставка")
    plt.plot(count_items, insert_time_rnd, 'o-', label="Рандом. дерево")
    plt.plot(count_items, insert_time_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для поиска
    plt.title("Поиск")
    plt.plot(count_items, search_time_rnd, 'o-', label="Рандом. дерево")
    plt.plot(count_items, search_time_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для удаления
    plt.title("Удаление")
    plt.plot(count_items, delete_time_rnd, 'o-', label="Рандом. дерево")
    plt.plot(count_items, delete_time_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для максимальной глубины
    plt.title("Максимальная глубина")
    plt.plot(count_items, max_depth_rnd, 'o-', label="Рандом. дерево")
    plt.plot(count_items, max_depth_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Максимальная глубина')
    plt.legend()
    plt.show()

    # Выводим в файл значения для посторения гистрограммы среднего распределения максимальной глубины
    my_file = open("max_depth.txt", "a+")
    my_file.write("AVL дерево:\n")
    my_file.write(str(int(max_depth_avl_last)))

    my_file.write("\nРандом. дерево:\n")
    my_file.write(str(int(max_depth_rnd_last)))
    my_file.close()

    # Выводим в файл значения для посторения гистрограммы среднего распределения глубин веток
    my_file = open("all_depths.txt", "a+")
    my_file.write("AVL дерево:\n")
    my_file.write(str(int(all_depths_avl)))

    my_file.write("\nРандом. дерево:\n")
    my_file.write(str(int(all_depths_rnd)))
    my_file.close()



















