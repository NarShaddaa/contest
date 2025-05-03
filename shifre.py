def decode_command(encoded: str) -> str:
    """
    Раскодирует строку, сжатую с помощью повторяющихся последовательностей.

    Принимает:
        encoded: Сжатая строка формата N[строка], например 3[a]2[bc].

    Возвращает:
        Раскодированная строка, например 'aaabcbc'.
    """
    stack: list[tuple[str, str]] = []
    buffer: str = ''
    number: str = ''

    for char in encoded:
        if '0' <= char <= '9':  # Явная проверка цифр
            number += char
        elif char == '[':
            stack.append((buffer, number))
            buffer = ''
            number = ''
        elif char == ']':
            prev_buffer, num_str = stack.pop()
            buffer = prev_buffer + buffer * int(num_str)  # в int
        else:
            buffer += char

    return buffer


if __name__ == '__main__':
    encoded_input = input().strip()
    print(decode_command(encoded_input))
