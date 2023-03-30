import random
import networkx as nx
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def generate_graph(num_vertices, max_edges, max_edges_per_vertex, is_directed, max_in_out_edges):
    # создаем граф
    G = nx.DiGraph() if is_directed else nx.Graph()
    # добавляем вершины
    G.add_nodes_from(range(num_vertices))
    # создаем случайное количество ребер
    num_edges = random.randint(0, max_edges)
    # добавляем случайные ребра
    while G.number_of_edges() < num_edges:
        # выбираем случайную пару вершин
        v1, v2 = random.sample(list(G.nodes()), 2)
        # проверяем, что ребра еще нет и максимальное количество ребер у вершины не превышено
        if G.number_of_edges(v1) < max_edges_per_vertex and G.number_of_edges(v2) < max_edges_per_vertex and not G.has_edge(v1, v2):
            # добавляем ребро
            G.add_edge(v1, v2)
            if not is_directed and random.choice([True, False]):
                G.add_edge(v2, v1)
    # создаем случайные количество входящих и выходящих ребер
    if is_directed:
        for v in G.nodes():
            num_in_edges = random.randint(0, max_in_out_edges)
            num_out_edges = random.randint(0, max_in_out_edges)
            in_edges = [e for e in G.in_edges(v)]
            out_edges = [e for e in G.out_edges(v)]
            while len(in_edges) < num_in_edges:
                # выбираем случайную вершину, не являющуюся текущей
                u = random.choice([u for u in G.nodes() if u != v])
                # добавляем ребро
                G.add_edge(u, v)
                in_edges.append((u, v))
            while len(out_edges) < num_out_edges:
                # выбираем случайную вершину, не являющуюся текущей
                u = random.choice([u for u in G.nodes() if u != v])
                # добавляем ребро
                G.add_edge(v, u)
                out_edges.append((v, u))
    return G


class Graph:
    def __init__(self, num_vertices, max_edges, max_edges_per_vertex, is_directed, max_in_out_edges):
        self.graph = generate_graph(num_vertices=num_vertices, max_edges=max_edges,
                                      max_edges_per_vertex=max_edges_per_vertex, is_directed=is_directed,
                                      max_in_out_edges=max_in_out_edges)

    # возвращаем матрицу смежности графа
    def adjacency_matrix(self):
        n = len(self.graph.nodes())
        # создаем пустую матрицу размера n x n, заполненную нулями
        matrix = np.zeros((n, n))
        # проходим по списку ребер и устанавливаем соответствующие значения элементов матрицы в 1
        for v1, v2 in self.graph.edges():
            matrix[v1][v2] = 1
            if not self.graph.is_directed():
                matrix[v2][v1] = 1
        return matrix

    # возвращаем матрицу инцидентности графа
    def incidence_matrix(self):
        # Получаем список всех ребер
        edges = list(self.graph.edges())
        # Создаем матрицу размера
        num_edges = len(edges)
        num_vertices = self.graph.number_of_nodes()
        inc_matrix = np.zeros((num_vertices, num_edges))
        # Заполняем матрицу инцидентности
        if self.graph.is_directed():
            for i, (u, v) in enumerate(edges):
                inc_matrix[u][i] = 1
                inc_matrix[v][i] = -1
        else:
            for i, (u, v) in enumerate(edges):
                inc_matrix[u][i] = 1
                inc_matrix[v][i] = 1
        return inc_matrix

    # возвращаем список смежности графа
    # ключи - вершины графа, а значения - списки смежных вершин
    def adjacency_list(self):
        # Создаем пустой словарь, который будет использоваться для хранения списка смежности
        adj_list = {}
        for u, v in self.graph.edges():
            # Проверяем, есть ли вершина u или v в словаре, и если ее нет, то добавляем эту вершину в словарь со значением по умолчанию - пустым списком []
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            # Добавляем вершину v в список смежности для вершины u
            adj_list[u].append(v)
            # Если граф неориентированный, то добавляем вершину u в список смежности для вершины v
            if not self.graph.is_directed():
                adj_list[v].append(u)
        return adj_list

    # возвращаеv список всех ребер графа
    def edge_list(self):
        edges = []
        # Проходимся по всем ребрам графа и добавляем их в список, u и v - вершины, которые соединяет это ребро
        for u, v in self.graph.edges():
            edges.append((u, v))
        return edges

    # поиск кратчайшего пути в графе с помощью алгоритма поиска в ширину
    def shortest_path_bfs(self, start_node, end_node):
        # Добавляем стартовую вершину в очередь и отмечаем ее как посещенную
        queue = [(start_node, [start_node])]
        visited = {start_node}

        # Если начальная вершина и конечная вершина совпадают, то возвращаем единичный путь
        if start_node == end_node:
            return [start_node]

        # Ищем путь от start до end, обрабатывая каждую вершину в очереди
        while queue:
            node, path = queue.pop(0)
            neighbors = self.graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor == end_node:
                        return path + [neighbor]
                    else:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

        # Если мы дошли до конца очереди и не нашли конечную вершину, то путь не существует
        return None

    # поиск кратчайшего пути в графе с помощью алгоритма поиска в глубину
    def shortest_path_dfs(self, start_node, end_node, path=None, shortest=None):
        # Если путь не был передан как аргумент, инициализируем его пустым списком
        if path is None:
            path = []

        # Добавляем начальную вершину в путь
        path = path + [start_node]

        # Если начальная вершина и конечная вершина совпадают, то мы нашли искомый путь и возвращаем его
        if start_node == end_node:
            return path

        # Для каждой вершины, смежной с начальной, выполняем следующие действия
        for node in self.graph[start_node]:
            # Если данная вершина не принадлежит текущему пути, то продолжаем поиск
            if node not in path:
                # Если кратчайший путь ещё не найден или текущий путь короче ранее найденного, то запускаем
                # рекурсивный поиск пути из данной вершины
                if shortest is None or len(path) < len(shortest):
                    newpath = self.shortest_path_dfs(node, end_node, path, shortest)
                    # Если путь найден, то присваиваем его кратчайшему пути
                    if newpath is not None:
                        shortest = newpath

        # Возвращаем кратчайший путь, если он найден, иначе - None
        return shortest

    def nodes(self):
        return self.graph.nodes()


if __name__ == '__main__':
    vertices_list = [50, 250, 150, 200, 250, 300, 350, 400, 450, 500]
    edges_list = [150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500]
    max_edges_per_vertex = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
    max_in_out_edges = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    bfs_times = []
    dfs_times = []

    for i in range(10):
        graph = Graph(num_vertices=vertices_list[i], max_edges=edges_list[i], max_edges_per_vertex=max_edges_per_vertex[i], is_directed=False, max_in_out_edges=max_in_out_edges[i])
        start_node, end_node = random.sample(list(graph.nodes()), 2)
        print(f"\nТест №{i + 1}:")

        # print("Матрица смежности графа:")
        # print(*graph.adjacency_matrix(), sep='\n')
        # print()
        # print("Матрица инцидентности графа:")
        # print(*graph.incidence_matrix(), sep='\n')
        # print()
        # print("Список смежности графа:")
        # print(graph.adjacency_list())
        # print()
        # print("Список всех ребер графа:")
        # print(graph.edge_list())

        start_time = timer()
        bfs_path = graph.shortest_path_bfs(start_node, end_node)
        end_time = timer()
        bfs_time = end_time - start_time
        bfs_times.append(bfs_time)

        if bfs_path:
            print(f"Поиск в ширину:")
            print(f"Кратчайший путь: {len(bfs_path)}")
            print(f"Время выполнения: {round(bfs_time, 5)}")


        start_time = timer()
        dfs_path = graph.shortest_path_dfs(start_node, end_node)
        end_time = timer()
        dfs_time = end_time - start_time
        dfs_times.append(dfs_time)

        if dfs_path:
            print(f"Поиск в глубину:")
            print(f"Кратчайший путь: {len(dfs_path)}")
            print(f"Время выполнения: {round(dfs_time, 5)}")

    plt.grid(True)
    plt.title("Поиск путей в графах")
    plt.xlabel("Количество вершин графа")
    plt.ylabel("Время выполнения")
    plt.plot(vertices_list, bfs_times, label="Поиск в ширину")
    plt.plot(vertices_list, dfs_times, label="Поиск в глубину")
    plt.legend()
    plt.show()

