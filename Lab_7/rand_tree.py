import random

class Node:
    def __init__(self, key):
        self.key = key
        self.size = 1
        self.right = None
        self.left = None

class RandTree:
    # Функция для поиска ершины с заданным значением
    def search(self, p, k):
        # Если дерево пустое
        if not p:
            return None

        # Если значение найдено
        if k == p.key:
            return p

        # Если значение меньше значения вершины, рекурсивно ищем в левом потомке
        if k < p.key:
            return self.search(p.left, k)
        else:
            # Если значение больше значения вершины, рекурсивно ищем в правом потомке
            return self.search(p.right, k)

    # Вспомогательная функция для получения размера узла
    def _getsize(self, p):
        if not p:
            return 0
        return p.size

    # Вспомогательная функция для установления корректного размера дерева
    def _fixsize(self, p):
        p.size = self._getsize(p.left) + self._getsize(p.right) + 1

    # Функция для правого поворота
    def _rotateright(self, p):
        # Новой вершине присваивается значение левого потомка родительской вершины
        q = p.left
        # Левому потомку родительской вершины присваивается значение правого потомка новой вершины
        p.left = q.right
        # Правому потомку новой вершины присваивается значение родительской вершиной
        q.right = p

        # Пересчитываем размеры узлов
        q.size = p.size
        self._fixsize(p)
        return q

    def _rotateleft(self, q):  # левый поворот вокруг узла q
        # Новой вершине присваивается значение левого потомка родительской вершины
        p = q.right
        # Правому потомку родительской вершины присваивается значение левого потомка новой вершины
        q.right = p.left
        # Левому потомку новой вершины присваивается значение родительской вершиной
        p.left = q

        # Пересчитываем размеры узлов
        p.size = q.size
        self._fixsize(q)
        return p

    # Вспомогательная функция для вставки вершины
    def _insertroot(self, p, k):
        # Если дерево пустое, то добавляем вершину в качестве корня
        if not p:
            return Node(k)
        # Если родительская вершина больше добавляемого значения
        if k < p.key:
            p.left = self._insertroot(p.left, k)
            return self._rotateright(p)
        else:
            p.right = self._insertroot(p.right, k)
            return self._rotateleft(p)

    # Функция рандомизированной вставки новой вершины
    def insert(self, p, k):
        # Если дерево пустое, то добавляем вершину в качестве корня
        if not p:
            return Node(k)

        # С вероятностью 1/(p.size+1) добавляем вершину в корень дерева
        if random.randint(0, p.size) == 0:
            return self._insertroot(p, k)
        # Если родительская вершина больше добавляемого значения
        if p.key > k:
            p.left = self.insert(p.left, k)
        else:
            # Если родительская вершина меньше добавляемого значения
            p.right = self.insert(p.right, k)

        # Пересчитываем размеры узлов
        self._fixsize(p)
        return p

    # Вспомогательная функция объединения двух деревьев
    def _join(self, p, q):
        # Если один из корней отсутвует, то возвращаем другой
        if not p:
            return q
        if not q:
            return p

        # Если случайное число меньше размера первого дерева, то оно становится корнем нового дерева
        if random.randint(0, p.size + q.size) < p.size:
            p.right = self._join(p.right, q)
            # Пересчитываем размер дерева
            self._fixsize(p)
            return p
        else:
            # Eсли случайное число больше размера первого дерева, то корнем нового дерева становится второе дерево
            q.left = self._join(p, q.left)
            # Пересчитываем размер дерева
            self._fixsize(q)
            return q

    # Функция для удаления вершины
    def delete(self, p, k):
        if not p:
            return p
        # Если значение вершины равно искомому значению
        if p.key == k:
            q = self._join(p.left, p.right)
            return q
        # Если значение вершины больше искомого значения
        elif k < p.key:
            # Вызываем функцию для левого потомка
            p.left = self.delete(p.left, k)
        else:
            # Если значение вершины меньше искомого значения
            # Вызываем функцию для правого потомка
            p.right = self.delete(p.right, k)
        return p

    # Функция для вычисления максимальной глубины дерева
    def max_depth(self, node):
        if not node:
            return 0
        # Вызываем функцию для левого потомка
        left_depth = self.max_depth(node.left)
        # Вызываем функцию для правого потомка
        right_depth = self.max_depth(node.right)
        # Возвращаем максимальную глубину из глубин левого и правого поддеревьев, увеличенную на 1 (текущий уровень)
        return max(left_depth, right_depth) + 1

    # Функция для вычисления глубин всех веток дерева
    def all_depths(self, node):
        if node is None:
            return []
        else:
            # Создаем пустой список, в который будем добавлять глубины потомков
            depths = []
            # Для левого и правого потомка
            for child in [node.left, node.right]:
                # Рекурсивно вызываем функцию, чтобы получить список глубин его потомков
                child_depths = self.all_depths(child)
                # Каждую глубину из полученного списка добавляем в основной список
                for depth in child_depths:
                    depths.append(depth + 1)
            # Если список пустой, то добавляем 1, т.к. корень существует
            if len(depths) == 0:
                depths.append(1)
            return depths