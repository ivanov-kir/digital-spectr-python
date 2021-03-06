"""Задание 1
Сформировать список из n точек на декартовой плоскости (х,у).
Заполнять значения координат точек случайными целыми числами (-100, 100).
Расположить точки в порядке обхода против часов стрелки, начиная с точки,
ближайшей к оси <у>, лежащей в координатном углу I (положительные абсциссы и ординаты), если есть таковые.
Найти среднее, мин., макс. расстояния точек от центра координатной плоскости (0,0). Вывести результаты на экран.
Размер исходного списка n задается пользователем вручную после запуска программы.
"""
from random import randint, seed
from math import sqrt
from timeit import default_timer
from sys import maxsize

import matplotlib.pyplot as plt

if __name__ == '__main__':
    seed(100)
    n = input('n = ')

    start_time = default_timer()

    coordinates = []
    max_distance = -maxsize
    max_coordinates = ()
    min_distance = maxsize
    min_coordinates = ()
    sum_distances = 0
    i = 0

    for _ in range(int(n)):
        i += 1

        x = randint(-100, 100)
        y = randint(-100, 100)
        coordinates.append((x, y))

        distance = sqrt(pow(x - 0, 2) + pow(y - 0, 2))
        if distance < min_distance:
            min_distance = distance
            min_coordinates = (x, y)
        if distance > max_distance:
            max_distance = distance
            max_coordinates = (x, y)
        sum_distances += distance

    print(f'min={min_distance}\nmax={max_distance}\nmean={sum_distances / i}')
    print(f'Performance time: {default_timer() - start_time}')

    plt.scatter(*zip(*coordinates), s=3, c='#DC143C')
    plt.plot(*zip(min_coordinates, (0, 0)), linewidth=5, linestyle='-', c='#4169E1')
    plt.plot(*zip(max_coordinates, (0, 0)), linestyle='-', c='#FF4500')
    plt.legend(labels=(f'min = {min_distance}', f'max = {max_distance}', f'mean = {sum_distances / i}'))
    plt.title('Расположение точек')
    plt.axhline(linestyle='--', c='k')
    plt.axvline(linestyle='--', c='k')
    plt.show()

    # Второй вариант решения (без графика)
    # start_time = default_timer()
    # coordinates = [(randint(-100, 100), randint(-100, 100))
    #                for _ in range(int(n))]
    #
    # distances = []
    # for coordinate in coordinates:
    #     x = coordinate[0]
    #     y = coordinate[1]
    #     distances.append(sqrt(pow(x - 0, 2) + pow(y - 0, 2)))
    #
    # min_ = min(distances)
    # max_ = max(distances)
    # mean = sum(distances) / len(distances)
    #
    # print(f'min={min(distances)}\nmax={max(distances)}\nmean={sum(distances) / len(distances)}')
    # print(f'Performance time: {default_timer() - start_time}')
