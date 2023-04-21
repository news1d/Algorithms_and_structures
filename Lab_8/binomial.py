from math import inf
class Node:
    def __init__(self, key):
        self.key = key          # Ключ узла
        self.degree = 0         # Степень узла
        self.parent = None      # Родитель узла
        self.child = None       # Потомок узла
        self.sibling = None     # "Брат" узла

class BinomialHeap:
    def __init__(self):
        self.head = None

    # Функция для поиска минимального ключа в куче
    def get_min(self):
        min_node = None
        current = self.head
        min_val = inf       # Инициализируем мин. значение как бесконечность
        # Проходим по всем узлам кучи
        while current:
            # Если значение текущего узла меньше минимального, обновляем минимальное значение
            if current.key < min_val:
                min_val = current.key
                min_node = current
            current = current.sibling
        return min_node.key

    # Вспомогательная функция, которая добавляет новый узел в список дочерних узлов корневого узла
    def _tree_link(self, new_child, root):
        # Если ключ корня больше ключа нового потомка
        if root.key > new_child.key:
            return 0
        # Если новый потомок или корень равны отсутствуют
        if new_child is None or root is None:
            return 0
        # Устанавливаем корень в качестве родителя для нового потомка
        new_child.parent = root
        # Устанавливаем нового потомка в качестве первого дочернего элемента корня
        new_child.sibling = root.child
        # Обновляем ссылку на первый дочерний элемент корня на нового потомок
        root.child = new_child
        # Увеличиваем степень корня на 1
        root.degree += 1

    # Вспомогательная функция, которая добавляет биномиальные деревья в порядке степеней
    def _heap_merge(self, other_heap):
        # Устанавливаем ссылки на корни каждой кучи
        x_node = self.head
        y_node = other_heap.head
        # Переменная для хранения выбранного узла на каждой итерации
        selected = None
        # Переменная для хранения корневого узла объединенной кучи
        head_node = None
        # Переменная для хранения предыдущего узла на каждой итерации
        prev_node = None

        # Пока есть хотя бы один узел в одной из куч
        while x_node or y_node:
            # Если узел x_node отсутствует, то выбираем y_node
            if x_node is None:
                selected = y_node
                y_node = y_node.sibling
            # Если узел y_node отсутствует, то выбираем x_node
            elif y_node is None:
                selected = x_node
                x_node = x_node.sibling
            # Если степень узла x_node меньше или равна степени узла y_node, то выбираем x_node
            elif x_node.degree <= y_node.degree:
                selected = x_node
                x_node = x_node.sibling
            # Если степень узла y_node меньше степени узла x_node, то выбираем y_node
            else:
                selected = y_node
                y_node = y_node.sibling

            # Если еще не был выбран корневой узел, то выбираем его (только для первой итерации)
            if head_node is None:
                head_node = selected
            # Иначе, устанавливаем выбранный узел как следующий узел для предыдущего узла
            else:
                prev_node.sibling = selected

            # Обновляем предыдущий узел
            prev_node = selected

        # Возвращаем корневой узел объединенной кучи
        return head_node

    # Вспомогательная функция, которая объединяет две кучи
    def _union(self, other_heap):
        # Создаем новую кучу
        unite = BinomialHeap()

        # Объединяем две кучи и устанавливаем корневой узел объединенной кучи
        unite.head = self._heap_merge(other_heap)
        # Если объединенная куча пуста, то возвращаем ее
        if unite.head is None:
            return unite

        # Инициализируем переменные для хранения текущего, предыдущего и следующего узла
        prev = None
        current = unite.head
        next = current.sibling

        # Проходим по всем узлам новой кучи
        while next:
            # Если текущий узел и следующий узел имеют разные степени или
            # степень текущего узла равна степени узла после следующего,
            # перемещаемся к следующему узлу
            if (current.degree != next.degree or
                    next.sibling is not None and next.sibling.degree == current.degree):
                prev = current
                current = next
                # Если степень текущего узла меньше степени следующего узла, выбираем текущий узел
            else:
                # Если значение текущего узла меньше или равно значению следующего, то связываем их между собой
                if current.key <= next.key:
                    current.sibling = next.sibling
                    self._tree_link(next, current)
                else:
                    # Если предыдущий узел отсутсвует, обновляем корень новой кучи на следующий узел
                    if prev is None:
                        unite.head = next
                    else:
                        prev.sibling = next

                    # Связываем текущий узел и следующий между собой
                    self._tree_link(current, next)
                    current = next

            # Обновляем следующий узел
            next = current.sibling

        # Возвращаем объединенную кучу
        return unite

    # Функция для вставки узла в биномиальную кучу
    def insert(self, key):
        # Создаем новый узел и сохраняем его в переменной node
        node = Node(key)
        # Создаем новую биномиальную кучу с одним элементом
        single = BinomialHeap()
        # Кореню новой кучи присваиваем узел node
        single.head = node
        # Объединяем текущую кучу с single кучей и присваиваем ее корень текущей куче
        self.head = self._union(single).head

    # Функция для удаления  узла с минимальным значением
    def delete_min(self):
        # Если биномиальная куча отсутствует
        if self.head is None:
            return 0

        # Инициализируем предыдущий узел, узел с минимальным значением и левого потомка
        prev = None
        min_node = None
        left_sibling = None
        # Устанавливаем корневой узел в качестве текущего
        current = self.head
        # Инициализируем мин. значение как бесконечность
        min_val = inf

        # Проходимся по всем узлам
        while current:
            # Проверяем, является ли текущий узел минимальным
            if current.key < min_val:
                # Обновляем переменные
                min_val = current.key
                min_node = current
                prev = left_sibling
            left_sibling = current
            current = current.sibling

        # Удаляем минимальный узел из кучи
        if prev is None:
            self.head = min_node.sibling
        else:
            prev.sibling = min_node.sibling

        # Создаем новую кучу
        heap = BinomialHeap()
        # Присваем переменной node значения потомка удаленного узла
        node = min_node.child

        # Проходим по всем потомкам удаленного узла и добавляем их в новую кучу
        while node:
            # Сохраняем ссылку на следующий узел перед изменением ссылок текущего узла
            next = node.sibling
            # Отсоединяем узел от его родителя
            node.parent = None
            # Добавляем узел в кучу, сделав его корневым элементом
            node.sibling = heap.head
            heap.head = node
            # Переходим к следующему дочернему узлу
            node = next

        # Объединяем новую кучу с оставшимися кучами.
        self.head = self._union(heap).head
        return min_node