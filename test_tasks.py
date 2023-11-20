from seminar6_task1 import Tasks, Person, Bank
import pytest
import unittest.mock


def test_find_average():
    assert Tasks.find_average([1, 2, 3]) == 2, 'Ошибка в работе функции'
    assert Tasks.find_average([]) == 0, 'Ошибка в работе функции'
    assert Tasks.find_average([5]) == 5, 'Ошибка в работе функции'


def test_find_average_type():  # перехватываем ошибку TypeError с помощью библиотеку pytest.raises
    with pytest.raises(TypeError):
        Tasks.find_average("qwerty")  # ожидаем получить ошибку TypeError


def test_person_bank_interaction():
    person = Person(1000)
    bank = Bank()
    person.transfer_money(bank, 500)
    assert person.balance == 500
    assert bank.balance == 500


def test_transfer_mock():
    mock_bank = unittest.mock.Mock()
    person = Person(1000)
    person.transfer_money(mock_bank, 500)
    mock_bank.recive_money.assert_called_with(500) #проверяем, что моп объект был вызван в методе



