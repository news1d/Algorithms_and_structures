class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Вспомогательная функция для получения высоты узла
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    # Вспомогательная функция для получения баланс-фактора узла
    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Получение узла с минимальным значением из дерева
    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    # Функция для правого поворота
    def _right_rotate(self, node):
        # Новой вершине присваивается значение левого потомка родительской вершины
        new_root = node.left
        # Левому потомку родительской вершины присваивается значение правого потомка новой вершины
        node.left = new_root.right
        # Правому потомку новой вершины присваивается значение родительской вершиной
        new_root.right = node

        # Пересчитываем высоты узлов
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    # Функция для левого поворота
    def _left_rotate(self, node):
        # Новой вершине присваивается значение левого потомка родительской вершины
        new_root = node.right
        # Правому потомку родительской вершины присваивается значение левого потомка новой вершины
        node.right = new_root.left
        # Левому потомку новой вершины присваивается значение родительской вершиной
        new_root.left = node

        # Пересчитываем высоты узлов
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    # Функция для вставки вершины
    def _insert_node(self, node, value):
        # Если дерево пустое, то добавляем вершину в качестве корня
        if node is None:
            return AVLNode(value)
        # Если родительская вершина больше добавляемого значения
        elif value < node.value:
            node.left = self._insert_node(node.left, value)
        else:
            node.right = self._insert_node(node.right, value)

        # Обновляем высоту текущей вершины
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Получаем баланс-фактор текущей вершины
        balance_factor = self._get_balance_factor(node)

        # Если вершина несбалансирована, то выполняем соответствующие операции для балансировки дерева
        if balance_factor > 1:
            # Если баланс левого потомка неотрицательный
            if self._get_balance_factor(node.left) >= 0:
                # Правый поворот родительской вершины
                return self._right_rotate(node)
            else:
                # Левый поворот левого потомка
                node.left = self._left_rotate(node.left)
                # Правый поворот родительской вершины
                return self._right_rotate(node)
        if balance_factor < -1:
            # Если баланс правого узла неположительный
            if self._get_balance_factor(node.right) <= 0:
                # Левый поворот родительской вершины
                return self._left_rotate(node)
            else:
                # Правый поворот правого потомка
                node.right = self._right_rotate(node.right)
                # Левый поворот родительской вершины
                return self._left_rotate(node)

        return node

    def insert(self, value):
        self.root = self._insert_node(self.root, value)

    # Вспомогательная функция для удаления вершины
    def _delete_node(self, node, value):
        if node is None:
            return node

        # Если значение вершины больше искомого значения
        elif value < node.value:
            # Вызываем функцию для левого потомка
            node.left = self._delete_node(node.left, value)
        # Если значение вершины меньше искомого значения
        elif value > node.value:
            # Вызываем функцию для правого потомка
            node.right = self._delete_node(node.right, value)
        # Если значение вершины равно искомому значению
        else:
            # Если вершина с одним или без потомков
            if node.left is None and node.right is None:
                node = None
                return node
            elif node.left is None:
                node = node.right
                return node
            elif node.right is None:
                node = node.left
                return node

            # Узел с двумя потомками
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_node(node.right, temp.value)

        # Если дерево имело только одну вершину, то возвращаем его
        if node is None:
            return node

        # Обновляем высоту текущего узла
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Получаем баланс-фактор текущего узла
        balance_factor = self._get_balance_factor(node)

        # Если вершина несбалансирована, то выполняем соответствующие операции для балансировки дерева
        if balance_factor > 1:
            # Если баланс левого потомка неотрицательный
            if self._get_balance_factor(node.left) >= 0:
                # Правый поворот родительской вершины
                return self._right_rotate(node)
            else:
                # Левый поворот левого потомка
                node.left = self._left_rotate(node.left)
                # Правый поворот родительской вершины
                return self._right_rotate(node)
        if balance_factor < -1:
            # Если баланс правого узла неположительный
            if self._get_balance_factor(node.right) <= 0:
                # Левый поворот родительской вершины
                return self._left_rotate(node)
            else:
                # Правый поворот правого потомка
                node.right = self._right_rotate(node.right)
                # Левый поворот родительской вершины
                return self._left_rotate(node)

        return node

    # Функция для удаления вершины
    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    # Вспомогательная функция для поиска ершины с заданным значением
    def _search_node(self, node, value):
        # Если дерево пустое или значение найдено
        if node is None or node.value == value:
            return node

        # Если значение меньше значения вершины, рекурсивно ищем в левом потомке
        if value < node.value:
            return self._search_node(node.left, value)
        else:
            # Если значение больше значения вершины, рекурсивно ищем в правом потомке
            return self._search_node(node.right, value)

    # Функция для поиска ершины с заданным значением
    def search(self, value):
        return self._search_node(self.root, value)

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