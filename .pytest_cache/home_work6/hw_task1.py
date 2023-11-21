class Task:

    # Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
    # a. Рассчитывает среднее значение каждого списка.
    # b. Сравнивает эти средние значения и выводит соответствующее сообщение:
    # - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
    # - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
    # - ""Средние значения равны"", если средние значения списков равны.

    def comparison_average(first_numbers: list, second_numbers: list) -> float:
        if not isinstance(first_numbers or second_numbers, list):
            raise TypeError('not list')
        if not first_numbers or not second_numbers:  # len(numbers) == 0
            return 0
        first_average = sum(first_numbers) / len(first_numbers)
        second_average = sum(second_numbers) / len(second_numbers)
        if first_average > second_average:
            return "Первый список имеет большее среднее значение"
        if second_average > first_average:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
