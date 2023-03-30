import random
import time
import numpy as np
import matplotlib.pyplot as plt


def generate_graph(vertices, min_edges):
    # Создаем пустой граф
    G = {}
    # Добавляем вершины
    for i in range(vertices):
        G[i] = {}
    # Задаем случайное количество связей каждой вершины
    for i in range(vertices):
        num_edges = random.randint(min_edges, int(vertices / 2))
        # Соединяем вершины случайными ребрами с весами от 1 до 20
        for j in random.sample(range(vertices), num_edges):
            if i != j:
                G[i][j] = random.randint(1, 20)
                G[j][i] = G[i][j]
    return G


def adjacency_matrix(graph):
    n = len(graph)
    # создаем пустую матрицу размера n x n, заполненную нулями
    matrix = np.zeros((n, n), dtype=int)
    # проходим по списку ребер и устанавливаем соответствующие значения элементов матрицы весов
    for u in graph:
        for v, w in graph[u].items():
            matrix[u][v] = w
            matrix[v][u] = w
    return matrix


def dijkstra(graph):
    # Находим кратчайшие пути между всеми парами вершин
    for i in range(len(graph)):
        dist = {j: float('inf') for j in graph}
        dist[i] = 0
        prev = {j: None for j in graph}
        visited = list()
        while len(visited) < len(graph):
            # Находим вершину с минимальным расстоянием до начальной вершины
            min_dist = float('inf')
            min_vertex = None
            for vertex in graph:
                if vertex not in visited and dist[vertex] < min_dist:
                    min_dist = dist[vertex]
                    min_vertex = vertex
            # Обновляем расстояния до смежных вершин
            for neighbor, weight in graph[min_vertex].items():
                if dist[min_vertex] + weight < dist[neighbor]:
                    dist[neighbor] = dist[min_vertex] + weight
                    prev[neighbor] = min_vertex
            visited.append(min_vertex)
        # Выводим длину кратчайшего пути и пройденные вершины
        for j in range(i+1, len(graph)):
            path = [j]
            vertex = j      # Конечная вершина
            while prev[vertex] is not None:
                path.append(prev[vertex])
                vertex = prev[vertex]
            path.reverse()
            print(f"Кратчайшим путем между вершинами {i} и {j} является {path} и равен {dist[j]}")


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
        print(f"\nМатрица смежности для графа с {len(graph)} вершинами:")
        print(adjacency_matrix(graph), sep='\n')

    # Задаем количество тестов
    num_tests = 5
    for i in range(len(num_vertices)):
        for j in range(num_tests):
            graph = generate_graph(vertices=num_vertices[i], min_edges=num_min_edges[i])
            print(f'\nТест {j + 1}/{num_tests} для графа с {len(graph)} вершинами')
            dijkstra(graph)

    # Создаем список для хранения времени
    times = []
    # Запускаем тесты для каждого графа и сохраняем время выполнения
    for graph in graphs_list:
        start_time = time.time()
        dijkstra(graph)
        end_time = time.time()
        times.append(end_time - start_time)

    # Строим график
    plt.plot(num_vertices, times, 'o-')
    plt.xlabel('Количество вершин')
    plt.ylabel('Затраченное время (мс)')
    plt.show()