from binary_tree import Node, Tree
from avl_tree import AVLNode, AVLTree
import sys
import random
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**6) # устанавливаем максимальную глубину рекурсии в 1 миллион вызовов

if __name__ == '__main__':
    count_items = []
    # Списки для хранения времени вставки в бинарное дерево неотсортированного и отсортированного списка
    insert_time_bin = []
    insert_time_bin_sorted = []

    # Списки для хранения времени поиска в бинарном дереве неотсортированного и отсортированного списка
    search_time_bin = []
    search_time_bin_sorted = []

    # Списки для хранения времени удаления в бинарном дереве неотсортированного и отсортированного списка
    delete_time_bin = []
    delete_time_bin_sorted = []

    # Списки для хранения времени вставки в AVL дерево неотсортированного и отсортированного списка
    insert_time_avl = []
    insert_time_avl_sorted = []

    # Списки для хранения времени поиска в AVL дереве неотсортированного и отсортированного списка
    search_time_avl = []
    search_time_avl_sorted = []

    # Списки для хранения времени удаления в AVL дереве неотсортированного и отсортированного списка
    delete_time_avl = []
    delete_time_avl_sorted = []

    # Списки для хранения времени поиска в неотсортированного и отсортированного списке
    search_time_list = []
    search_time_list_sorted = []

    for i in range(1, 11):
        print(f"Серия №{i}")
        count_items.append(2 ** (10 + i))
        for j in range(2):
            num_list = random.sample(range(1, 3000000), 2 ** (10 + i))
            num_list_sorted = list(range(2 ** (10 + i)))

            # Цикл для несортированного списка
            if j < 10:
                BinTree = Tree()
                AvlTree = AVLTree()

                # Замеряем время вставки бинарного дерева
                start = time.time()
                for x in num_list:
                    BinTree.append(Node(x))
                end = time.time()
                insert_time_bin.append(end - start)

                # Замеряем время вставки AVL дерева
                start = time.time()
                for x in num_list:
                    AvlTree.insert(x)
                end = time.time()
                insert_time_avl.append(end - start)

                # Замеряем время поиска в бинарном дереве
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    BinTree.search(rand_number)
                end = time.time()
                search_time_bin.append(end - start)

                # Замеряем время поиска в AVL дереве
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    AvlTree.search(rand_number)
                end = time.time()
                search_time_avl.append(end - start)

                # Замеряем время поиска в векторе
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    try:
                        num_list.index(rand_number)
                    except:
                        None
                end = time.time()
                search_time_list.append(end - start)

                # Замеряем время удаления в бинарном дереве:
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    BinTree.del_node(rand_number)
                end = time.time()
                delete_time_bin.append(end - start)

                # Замеряем время удаления в AVL дереве:
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    AvlTree.delete(rand_number)
                end = time.time()
                delete_time_avl.append(end - start)

            # Цикл для сортированного списка
            if j >= 10:
                BinTree = Tree()
                AvlTree = AVLTree()

                # Замеряем время вставки бинарного дерева
                start = time.time()
                for x in num_list_sorted:
                    BinTree.append(Node(x))
                end = time.time()
                insert_time_bin_sorted.append(end - start)

                # Замеряем время вставки AVL дерева
                start = time.time()
                for x in num_list_sorted:
                    AvlTree.insert(x)
                end = time.time()
                insert_time_avl_sorted.append(end - start)

                # Замеряем время поиска в бинарном дереве
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    BinTree.search(rand_number)
                end = time.time()
                search_time_bin_sorted.append(end - start)

                # Замеряем время поиска в AVL дереве
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    AvlTree.search(rand_number)
                end = time.time()
                search_time_avl_sorted.append(end - start)

                # Замеряем время поиска в векторе
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    try:
                        num_list_sorted.index(rand_number)
                    except:
                        None
                end = time.time()
                search_time_list_sorted.append(end - start)

                # Замеряем время удаления в бинарном дереве:
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    BinTree.del_node(rand_number)
                end = time.time()
                delete_time_bin_sorted.append(end - start)

                # Замеряем время удаления в AVL дереве:
                start = time.time()
                for x in range(1000):
                    rand_number = random.randint(1, 3000000)
                    AvlTree.delete(rand_number)
                end = time.time()
                delete_time_avl_sorted.append(end - start)

    # Строим график для вставки (обычный)
    plt.title("Вставка (обычный)")
    plt.plot(count_items, insert_time_bin, 'o-', label="Бинарное дерево")
    plt.plot(count_items, insert_time_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для вставки (отсортированный)
    plt.title("Вставка (отсортированный)")
    plt.plot(count_items, insert_time_bin_sorted, 'o-', label="Бинарное дерево")
    plt.plot(count_items, insert_time_avl_sorted, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для поиска (обычный)
    plt.title("Поиск (обычный)")
    plt.plot(count_items, search_time_bin, 'o-', label="Бинарное дерево")
    plt.plot(count_items, search_time_avl, 'o-', label="AVL дерево")
    plt.plot(count_items, search_time_list, 'o-', label="Массив")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для поиска (отсортированный)
    plt.title("Поиск (отсортированный)")
    plt.plot(count_items, search_time_bin_sorted, 'o-', label="Бинарное дерево")
    plt.plot(count_items, search_time_avl_sorted, 'o-', label="AVL дерево")
    plt.plot(count_items, search_time_list_sorted, 'o-', label="Массив")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для удаления (обычный)
    plt.title("Удаление (обычный)")
    plt.plot(count_items, delete_time_bin, 'o-', label="Бинарное дерево")
    plt.plot(count_items, delete_time_avl, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()

    # Строим график для удаления (отсортированный)
    plt.title("Удаление (отсортированный)")
    plt.plot(count_items, delete_time_bin_sorted, 'o-', label="Бинарное дерево")
    plt.plot(count_items, delete_time_avl_sorted, 'o-', label="AVL дерево")
    plt.xlabel('Количество элементов')
    plt.ylabel('Затраченное время (мс)')
    plt.legend()
    plt.show()