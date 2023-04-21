class BinaryHeapMax():
    # Инициализируем пустую кучу с единичным корнем
    def __init__(self):
        self.heap = [0]
        self.size = 0

    # Функция для вставки элемента в кучу
    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self._perc_up(self.size)

    # Вспомогательная функция, которая поднимает элемент, если он больше своего родителя
    def _perc_up(self, i):
        # Пока родительский элемент существует, продолжаем перестраивать кучу
        while i // 2 > 0:
            # Если элемент больше своего родителя, меняем их местами
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    # Функция, которая удаляем максимальный элемент
    def delete_max(self):
        # Если куча существует
        if self.heap and self.size > 0:
            # Сохраняем значение максимального элемента
            retval = self.heap[1]
            # Помещаем последний элемент на вершину кучи
            self.heap[1] = self.heap[self.size]
            # Уменьшаем размер кучи
            self.size -= 1
            # Удаляем последний элемент
            self.heap.pop()
            # Опускаем новый корень кучи на нужное место
            self._perc_down(1)
            return retval
        else:
            return 0

    # Вспомогательная функция, которая опускает элемент вниз, если он меньше своих потомков
    def _perc_down(self, i):
        # Пока у элемента i есть потомки, продолжаем перестраивать кучу
        while i * 2 <= self.size:
            # Находим наибольшего потомка элемента i
            mc = self._max_child(i * 2)
            # Если значение наибольшего потомка больше значения элемента i, меняем их местами
            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    # Вспомогательная функция, которая возвращает индекс наибольшего потомка элемента с заданным индексом
    def _max_child(self, i):
        # Если у элемента i только один потомок, возвращаем его
        if i + 1 > self.size:
            return i
        else:
            # Иначе сравниваем значения двух потомков и возвращаем индекс наибольшего
            if self.heap[i] > self.heap[i + 1]:
                return i
            else:
                return i + 1

    # Функция, которая возвращает максимальный элемент кучи
    def get_max(self):
        if self.heap and self.size > 0:
            return self.heap[1]
        return 0