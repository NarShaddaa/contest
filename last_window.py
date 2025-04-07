def length_of_longest_substring(s: str) -> int:
    char_index = {}  # Хранит последние индексы символов
    max_length = 0
    left = 0  # Левая граница окна

    for right in range(len(s)):
        current_char = s[right]
        # Если символ уже встречался и находится в текущем окне, сдвигаем left
        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1
        # Обновляем индекс текущего символа
        char_index[current_char] = right
        # Обновляем максимальную длину
        max_length = max(max_length, right - left + 1)

    return max_length


# Чтение ввода и вывод результата
s = input().strip()
print(length_of_longest_substring(s))
