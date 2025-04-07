def min_platforms(weights: list[int], limit: int) -> int:
    """Вычисляет минимальное количество платформ,
    необходимых для размещения роботов."""
    weights = sorted(weights)

    # Два указателя:
    # left - начало массива (самые легкие роботы)
    # right - конец массива (самые тяжелые роботы)
    left_index = 0
    right_index = len(weights) - 1

    # Счетчик необходимых платформ
    platforms = 0

    # Пока есть роботы для обработки (левая граница не перешла правую)
    while left_index <= right_index:
        # сажаем на одну платформу самого легкого и самого тяжелого
        if weights[left_index] + weights[right_index] <= limit:
            # Если их суммарный вес допустим, берем обоих
            # и переходим к следующему легкому роботу
            left_index += 1

        # В любом случае самого тяжелого робота сажаем на платформу:
        # либо с самым легким (если влез), либо одного (если не влез)
        right_index -= 1

        # Увеличиваем счетчик платформ после каждой итерации
        platforms += 1

    return platforms


if __name__ == "__main__":
    weights = [int(x) for x in input().split()]  # Массив весов роботов
    limit = int(input())                       # Грузоподъемность платформы

    # Результат
    print(min_platforms(weights, limit))
