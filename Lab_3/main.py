import datetime
import random

class Queue:

    def __init__(self, item=None):
        try:
            self.__queue = list(item)
        except Exception:
            self.__queue = list()

    # Добавляем элемент в конец
    def add(self, item) -> None:
        self.__queue.append(item)

    # Удаляем + возвращаем первый элемент
    def remove(self):
        if len(self.__queue) == 0:
            pass
        else:
            return self.__queue.pop(0)

    # Возвращаем длину
    def size(self):
        return len(self.__queue)

    # Проверка на пустоту
    def isempty(self) -> bool:
        return len(self.__queue) == 0

    # Возвращаем все элементы
    def get_queue(self):
        return self.__queue

    # Возвращаем объект итератора
    def __iter__(self):
        self.current = 0
        return self

    # Возвращаем следующий элемент очереди
    def __next__(self):
        if self.current < len(self.__queue):
            result = self.__queue[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration


def test_1():
    container = Queue()
    for i in range(0, 1000):
        container.add(random.randint(-1000, 1000))

    max = -2000
    min = 2000
    sum = 0
    for item in container:
        sum += item
        if item > max:
            max = item
        elif item < min:
            min = item

    avg = sum // container.size()
    print(f"TEST 1:\nMAX = {max}\nAVG = {avg}\nMIN = {min}\nSUM = {sum}")


def test_2():
    container = Queue()

    for i in range(0, 10):
        container.add(f"item_{i}")

    print("\nTEST 2:")
    print("Очередь до добавления элементов: ", end="")
    for item in container:
        print(item, end=" ")

    container.add("new")

    print("\nОчередь после добавления элементов: ", end="")
    for item in container:
        print(item, end=" ")

    container.remove()

    print("\nОчередь после удаления элементов: ", end="")
    for item in container:
        print(item, end=" ")


def test_3():
    container = Queue()
    name = ["Вадим", "Максим", "Егор", "Георгий", "Михаил", "Сергей", "Глеб", "Александр", "Анатолий", "Андрей"]
    surname = ["Дмитриев", "Смирнов", "Киселев", "Степанов", "Волков", "Петров", "Леонов", "Шаповалов", "Зубов", "Сидоров"]
    patronymic = ["Александрович", "Глебович", "Вадимович", "Федорович", "Борисович", "Игоревич", "Кириллович", "Максимович", "Павлович", "Николаевич"]
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    delta = end_date - start_date


    for i in range(0, 100):
        person = []

        random_days = random.randint(0, delta.days)
        random_date = start_date + datetime.timedelta(days=random_days)

        person.append(random.choice(name))
        person.append(random.choice(surname))
        person.append(random.choice(patronymic))
        person.append(random_date)

        container.add(person)

    less_than_20 = Queue()
    more_than_30 = Queue()
    other_people = Queue()
    for item in container:
        if ((datetime.date.today() - item[3]).days / 365) < 20:
            less_than_20.add(item)
        elif ((datetime.date.today() - item[3]).days / 365) > 30:
            more_than_30.add(item)
        else:
            other_people.add(item)
    print("\n\nTEST 3:")
    print(f"Количество людей старше 30 лет: {more_than_30.size()}")
    print(f"Количество людей младше 20 лет: {less_than_20.size()}")
    print(f"Количество остальных людей: {other_people.size()}")


def test_4():
    container = Queue()

    for i in range(0, 1000):
        container.add(random.randint(-1000, 1000))

    print("\nTEST 4:")
    print("Очередь до сортировки:")
    for item in container:
        print(item, end=" ")

    container = Queue(sorted(container.get_queue()))

    print("\nОчередь после сортировки:")
    for item in container:
        print(item, end=" ")

def test_5():
    container = Queue()

    for i in range(0, 1000):
        container.add(random.randint(-1000, 1000))

    print("\n\nTEST 5:")
    print("Исходная очередь:")
    for item in container:
        print(item, end=" ")

    container = Queue(sorted(container.get_queue()))

    print("\nОтсортированная очередь:")
    for item in container:
        print(item, end=" ")

    list_tmp = []
    while not container.isempty():
        list_tmp.append(container.remove())

    while len(list_tmp) > 0:
        container.add(list_tmp.pop())

    print("\nИнвертированная очередь:")
    for item in container:
        print(item, end=" ")


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
