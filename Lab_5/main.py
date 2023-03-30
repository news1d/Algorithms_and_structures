import random
import networkx as nx
import time
import numpy as np
import matplotlib.pyplot as plt

def generate_graph(vertices, min_edges):
    # Создаем пустой граф
    G = nx.Graph()
    # Добавляем вершины
    G.add_nodes_from(range(vertices))
    # Задаем случайное количество связей каждой вершины
    for i in range(vertices):
        num_edges = random.randint(min_edges, int(vertices / 2))
        # Соединяем вершины случайными ребрами с весами от 1 до 20
        for j in random.sample(range(vertices), num_edges):
            if i != j:
                G.add_edge(i, j, weight=random.randint(1, 20))
    return G

def adjacency_matrix(graph):
    n = graph.number_of_nodes()
    # создаем пустую матрицу размера n x n, заполненную нулями
    matrix = np.zeros((n, n))
    # проходим по списку ребер и устанавливаем соответствующие значения элементов матрицы в 1
    for u, v in graph.edges():
        w = graph[u][v]['weight']
        matrix[u][v] = w
        matrix[v][u] = w
    return matrix.astype(int)

def dijkstra(graph):
    # Находим кратчайшие пути между всеми парами вершин
    for i in range(graph.number_of_nodes()):
        dist, path = nx.single_source_dijkstra(graph, i)
        for j in range(i, graph.number_of_nodes()):
            if i == j:
                continue
            print(f"Кратчайшим путем между вершинами {i} и {j} является {path[j]} и он равен {dist[j]}")



if __name__ == '__main__':
    # Задаем количество вершин в графе
    num_vertices = [10, 20, 50, 100]
    num_min_edges = [3, 4, 10, 20]

    # Создаем список графов для каждого количества вершин
    graphs_list = []
    for i in range(len(num_vertices)):
        graph = generate_graph(vertices=num_vertices[i], min_edges=num_min_edges[i])
        graphs_list.append(graph)

    # Выводим матрицы смежности для каждого графа
    for graph in graphs_list:

        print(f"Матрица смежности для графа с {graph.number_of_nodes()} вершинами:")
        print(*adjacency_matrix(graph), sep='\n')
        print(nx.adjacency_matrix(graph).todense(), end='\n\n')

    # Задаем количество тестов
    num_tests = 5
    for i in range(len(num_vertices)):
        for j in range(num_tests):
            graph = generate_graph(vertices=num_vertices[i], min_edges=num_min_edges[i])
            print(f'\nТест {j + 1}/{num_tests} для графа с {graph.number_of_nodes()} вершинами')
            dijkstra(graph)

    # Создаем список для сохранения времени
    time_taken = []
    # Запускаем тесты для каждого графа и сохраняем время выполнения
    for graph in graphs_list:
        start_time = time.time()
        dijkstra(graph)
        time_taken.append(time.time() - start_time)


    # Строим график
    plt.plot(num_vertices, time_taken, 'o-')
    plt.xlabel('Количество вершин')
    plt.ylabel('Затраченное время (мс)')
    plt.show()