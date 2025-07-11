import math
import random
from pprint import pprint


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    hello = "Привет, "
    you = ' Тебе '
    years = " лет."
    output = hello + name + "!" + you + str(age) + years

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60

    area = a * b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    area = math.pow(r, 2) * math.pi

    assert area == 1661.9025137490005

    length = 2 * math.pi * r

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    random.seed('Anacondaz')
    # l1 = [1]
    # l2 = [random.randint(1, 100)]
    # l3 = [random.randint(1, 100)]
    # l4 = [random.randint(1, 100)]
    # l5 = [100]
    # l6 = [random.randint(1, 100)]
    # l7 = [random.randint(1, 100)]
    # l8 = [random.randint(1, 100)]
    # l9 = [random.randint(1, 100)]
    # l10 = [random.randint(1, 100)]
    # l = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10
    l = []
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    l.append(random.randint(1, 100))
    list.sort(l)
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # list.remove(l, 5)
    # list.remove(l, 5)
    # list.remove(l, 8)
    # list.remove(l, 10)
    l = list(set(l))
    print(l)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first, second))
    pprint(d)
    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second