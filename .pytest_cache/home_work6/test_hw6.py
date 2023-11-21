import pytest

from hw_task1 import Task


def test_comparison_average():
    assert Task.comparison_average([2, 2, 2], [3, 3, 3]) == "Второй список имеет большее среднее значение"
    assert Task.comparison_average([5, 5, 5], [3, 3, 3]) == "Первый список имеет большее среднее значение"
    assert Task.comparison_average([3, 3, 3], [3, 3, 3]) == "Средние значения равны"
    assert Task.comparison_average([], [3, 3, 3]) == 0
    assert Task.comparison_average([1, 1, 1], []) == 0


def test_comparison_average_type():  # перехватываем ошибку TypeError
    with pytest.raises(TypeError):
        Task.comparison_average("qwerty", [1, 1, 1])
