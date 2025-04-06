def find_first_position(sorted_arr, target):
    left = 0
    right = len(sorted_arr) - 1
    result = -1  # элемент не найден

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            result = mid  # найденная позиция
            right = mid - 1  # ищем слева
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Если элемент не найден, возвращаем позицию вставки
    return result if result != -1 else left


# Пример
arr = [int(x) for x in input().split()]
target = int(input())
print(find_first_position(arr, target))
