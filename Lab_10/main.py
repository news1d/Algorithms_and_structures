import math
import random
import time
from scipy.stats import cauchy
import matplotlib.pyplot as plt

# Целевая функция
def F(x):
    return x ** 2 + 10 - 10 * math.cos(2 * math.pi * x)

def simulated_annealing(T0, alpha, x0, T_end):
    # Устанавливаем начальную температуру и начальное значение переменной x
    T = T0
    x = x0

    # Запускаем цикл, пока температура не достигнет конечного значения
    while T > T_end:
        # Генерируем новое значение переменной x
        x_new = x + T * cauchy.rvs()
        # Вычисляем разность функций F(x_new) и F(x)
        delta_E = F(x_new) - F(x)

        # Если разность меньше нуля, то новое значение x принимается
        # Иначе принимаем новое значение x с вероятностью exp(-delta_E / T)
        if delta_E < 0 or math.exp(-delta_E / T) > random.uniform(0, 1):
            x = x_new

        # Уменьшаем температуру на величину alpha
        T -= alpha

    # Возвращаем найденное значение x и значение функции в этой точке
    return x, F(x)


if __name__ == "__main__":

    # Инициализируем список минимальных температур и затраченного времени
    T_values = [1, 5, 10, 25, 50]
    times = []

    # Запускаем цикл по элементам списка температур и вычисляем затраченное время
    for T_end in T_values:
        start_time = time.time()
        simulated_annealing(T0=100, alpha=0.01, x0=0, T_end=T_end)
        end_time = time.time()
        times.append(end_time - start_time)

    # Создаем график
    fig, ax = plt.subplots()
    ax.set_title('График зависимости времени от минимальной температуры')
    ax.plot(T_values, times)
    ax.invert_xaxis()
    ax.set_xlabel('Минимальная температура')
    ax.set_ylabel('Затраченное время')
    plt.show()