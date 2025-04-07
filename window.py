from sys import maxsize


def find_min_slice_sum(data, elements_in_slice):
    if len(data) < elements_in_slice or elements_in_slice <= 0:
        return 0

    # Инициализация начальной суммы первого окна
    window_sum = sum(data[:elements_in_slice])
    min_sum = window_sum

    # Применяем алгоритм скользящего окна
    for i in range(1, len(data) - elements_in_slice + 1):
        # Вычитаем уходящий элемент и добавляем новый
        window_sum = window_sum - data[i-1] + data[i + elements_in_slice - 1]

        # Обновляем минимальную сумму
        if window_sum < min_sum:
            min_sum = window_sum

    return min_sum


if __name__ == '__main__':
    data = [5, -3, -2, 10, 2, 7, 1, -6, 13]
    elements_in_slice = 4
    # Вывод: -5 (сумма подмассива [-2, 10, 2, 7, 1, -6] не учитывается, так как нужна длина 4)
    print(find_min_slice_sum(data, elements_in_slice))
