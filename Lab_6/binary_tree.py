class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    # Ищем родительскую вершину, к которой будем добавлять новую вершину
    def __find(self, node, parent, value):
        # Если вершина не существует то
        if node is None:
            return None, parent, False
        # Если вершина с таким значением существует
        if value == node.data:
            return node, parent, True

        # Рекурсивно проходим по левой ветви
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        # Рекурсивно проходим по правой ветви
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    # Добавление вершин
    def append(self, obj):
        # Если в дерево пустое, то добавляем вершину в качестве корня
        if self.root is None:
            self.root = obj
            return obj

        # Ищем родительскую вершину, к которой будем добавлять новую вершину
        s, p, fl_find = self.__find(self.root, None, obj.data)

        # Если вершины с таким значением нет и родительская вершина существует
        if not fl_find and s:
            # Если родительская вершина больше добавляемого значения
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    # Удаляем одного потомка
    def __del_one_child(self, s, p):
        # Если удаляемый потомок является левым
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        # Если удаляемый потомок является правым
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    # Ищем минимальную вершину
    def __find_min(self, node, parent):
        # Если левый потомок существует, то продолжаем рекурсию
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    # Удаляем вершину
    def del_node(self, key):
        # Ищем вершину с нужным значением
        s, p, fl_find = self.__find(self.root, None, key)

        # Вершина не найдена
        if not fl_find:
            return None

        # Если вершина не имеет потомков
        if s.left is None and s.right is None:
            if p.left == s:
                p.left = None
            elif p.right == s:
                p.right = None

        # Если вершина имеет только одного потомка
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)

        # Если вершина имеет обоих потомков
        else:
            # Ищем минимальную вершину в правом потомке
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    # Функция для поиска ершины с заданным значением
    def _search_helper(self, node, value):
        # Если дерево пустое или значение найдено
        if node is None or node.data == value:
            return node
        # Если значение меньше значения вершины, рекурсивно ищем в левом потомке
        if value < node.data:
            return self._search_helper(node.left, value)
        else:
            # Если значение больше значения вершины, рекурсивно ищем в правом потомке
            return self._search_helper(node.right, value)

    # Поиск вершины
    def search(self, value):
        return self._search_helper(self.root, value)